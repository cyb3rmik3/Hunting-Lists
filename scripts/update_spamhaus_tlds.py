#!/usr/bin/env python3
"""Refresh spamhaus-abused-tlds.csv from Spamhaus' ccTLD "All malicious domains" ranking.

Source page: https://www.spamhaus.org/reputation-statistics/cctlds/domains/
That page is rendered by JavaScript from a JSON API (and is served with an HTTP 404
status), so we read the API directly. Output keeps the original layout:
    TLD,Badness Index       (top 10; Spamhaus now calls the metric "Bad Reputation Score")
"""
import csv
import sys

import requests

from readme_date import update_readme_date

API = "https://www.spamhaus.org/api/v1/stats/tld/datasets/total/variants/country"
OUT = sys.argv[1] if len(sys.argv) > 1 else "spamhaus-abused-tlds.csv"
README = sys.argv[2] if len(sys.argv) > 2 else "README.md"
TOP_N = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; Hunting-Lists-updater; +https://github.com/cyb3rmik3/Hunting-Lists)"}


def parse(payload: dict):
    rankings = payload["data"]["rankings"]
    rankings = sorted(rankings, key=lambda r: r["rank"])
    return [("." + r["key"], f"{round(r['hits']['reputation_score'], 1):g}") for r in rankings]


def main():
    resp = requests.get(API, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    rows = parse(resp.json())[:TOP_N]
    if len(rows) != TOP_N or not all(len(t) > 2 and t.startswith(".") and float(s) >= 0 for t, s in rows):
        sys.exit(f"Unexpected data ({len(rows)} rows); refusing to overwrite {OUT}")
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["TLD", "Badness Index"])
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT}")
    update_readme_date(README, "| [spamhaus-abused-tlds]")


if __name__ == "__main__":
    main()

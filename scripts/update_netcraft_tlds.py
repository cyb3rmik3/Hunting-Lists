#!/usr/bin/env python3
"""Refresh netcraft-tlds.csv from https://trends.netcraft.com/cybercrime/tlds.

Keeps the existing CSV layout: TLD, Country/Name, Incidents to Sites Ratio
(top 20 rows, in the order Netcraft lists them: worst ratio first).
Refuses to overwrite the file if the page layout looks different.
"""
import csv
import datetime
import re
import sys

import requests
from bs4 import BeautifulSoup

URL = "https://trends.netcraft.com/cybercrime/tlds"
OUT = sys.argv[1] if len(sys.argv) > 1 else "netcraft-tlds.csv"
README = sys.argv[2] if len(sys.argv) > 2 else "README.md"
TOP_N = 20
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; Hunting-Lists-updater; +https://github.com/cyb3rmik3/Hunting-Lists)"}


def parse(html: str):
    soup = BeautifulSoup(html, "html.parser")
    for table in soup.find_all("table"):
        heads = [th.get_text(" ", strip=True).lower() for th in table.find_all("th")]
        try:
            i_tld = next(i for i, h in enumerate(heads) if "top level domain" in h or h == "tld")
            i_name = next(i for i, h in enumerate(heads) if "country" in h or "name" in h)
            i_ratio = next(i for i, h in enumerate(heads) if "ratio" in h)
        except StopIteration:
            continue
        rows = []
        for tr in table.find_all("tr"):
            tds = [td.get_text(" ", strip=True) for td in tr.find_all("td")]
            if len(tds) < len(heads):
                continue
            rows.append((tds[i_tld], tds[i_name], tds[i_ratio]))
        return rows
    raise RuntimeError("Netcraft table not found - page layout may have changed")


def update_readme(path: str):
    """Set the 'Last updated' date (DD/MM/YYYY, UTC) on the netcraft-tlds row."""
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y")
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    hit = 0
    for i, line in enumerate(lines):
        if line.startswith("| [netcraft-tlds]"):
            lines[i], n = re.subn(r"\|(\s*)\d{2}/\d{2}/\d{4}(\s*)\|", rf"|\g<1>{today}\g<2>|", line, count=1)
            hit += n
    if hit != 1:
        sys.exit("README netcraft-tlds row/date not found; refusing to guess")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))
    print(f"README last-updated set to {today}")


def main():
    resp = requests.get(URL, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    rows = parse(resp.text)[:TOP_N]
    if len(rows) != TOP_N or not all(r[0].startswith(".") and r[2].startswith("1 in") for r in rows):
        sys.exit(f"Unexpected data ({len(rows)} rows); refusing to overwrite {OUT}")
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["TLD", "Country/Name", "Incidents to Sites Ratio"])
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT}")
    update_readme(README)


if __name__ == "__main__":
    main()

"""Shared helper: set the 'Last updated' date on a README sources-table row."""
import datetime
import re
import sys


def update_readme_date(path: str, row_prefix: str) -> str:
    """Set DD/MM/YYYY (UTC today) in the first date cell of the row starting with row_prefix."""
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y")
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    hit = 0
    for i, line in enumerate(lines):
        if line.startswith(row_prefix):
            lines[i], n = re.subn(r"\|(\s*)\d{2}/\d{2}/\d{4}(\s*)\|", rf"|\g<1>{today}\g<2>|", line, count=1)
            hit += n
    if hit != 1:
        sys.exit(f"README row {row_prefix!r} / date not found; refusing to guess")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))
    print(f"README {row_prefix} last-updated set to {today}")
    return today

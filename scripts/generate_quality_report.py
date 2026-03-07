from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

DATASET_PATH = Path("data/raw/netflix_data.csv")
OUTPUT_PATH = Path("reports/data-quality-report.md")


def main() -> int:
    if not DATASET_PATH.exists():
        print(f"[ERROR] Missing dataset: {DATASET_PATH}")
        return 1

    df = pd.read_csv(DATASET_PATH)

    type_counts = df["type"].value_counts(dropna=False).to_dict() if "type" in df else {}
    country_top = (
        df["country"].fillna("Unknown").value_counts().head(10).to_dict()
        if "country" in df
        else {}
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Netflix Dataset Quality Report",
        "",
        f"Generated: {generated_at}",
        "",
        "## Snapshot",
        "",
        f"- Rows: {len(df):,}",
        f"- Columns: {len(df.columns)}",
        f"- Duplicate show_id rows: {int(df['show_id'].duplicated().sum()) if 'show_id' in df else 'N/A'}",
        "",
        "## Content mix (`type`)",
    ]

    if type_counts:
        for k, v in type_counts.items():
            lines.append(f"- {k}: {int(v):,}")
    else:
        lines.append("- Column `type` not available")

    lines.extend(["", "## Top countries", ""])

    if country_top:
        for k, v in country_top.items():
            lines.append(f"- {k}: {int(v):,}")
    else:
        lines.append("- Column `country` not available")

    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Report generated at {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

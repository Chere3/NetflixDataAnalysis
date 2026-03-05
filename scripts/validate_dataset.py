from __future__ import annotations

from pathlib import Path

from netflix_analysis.quality import validate_dataset

DATASET_PATH = Path("data/raw/netflix_data.csv")


def main() -> int:
    try:
        result = validate_dataset(DATASET_PATH)
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")
        return 1

    if result.missing_columns:
        print(f"[ERROR] Missing required columns: {sorted(result.missing_columns)}")
        return 1

    if result.duplicated_ids:
        print(f"[ERROR] Duplicated show_id rows detected: {result.duplicated_ids}")
        return 1

    print("[OK] Dataset schema validated")
    print(f"[INFO] Rows: {result.rows:,}")
    print(f"[INFO] Columns: {result.columns}")
    print("[INFO] Null values by required column:")
    for column, count in sorted(result.null_summary.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {column}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

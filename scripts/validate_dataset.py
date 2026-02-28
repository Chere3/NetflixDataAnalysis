from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

DATASET_PATH = Path('data/raw/netflix_data.csv')
REQUIRED_COLUMNS = {
    'show_id',
    'title',
    'type',
    'director',
    'cast',
    'country',
    'date_added',
    'release_year',
    'duration',
    'genre',
    'description',
}


def main() -> int:
    if not DATASET_PATH.exists():
        print(f'[ERROR] Missing dataset: {DATASET_PATH}')
        return 1

    df = pd.read_csv(DATASET_PATH)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        print(f'[ERROR] Missing required columns: {sorted(missing_columns)}')
        return 1

    duplicated_ids = int(df['show_id'].duplicated().sum())
    if duplicated_ids:
        print(f'[ERROR] Duplicated show_id rows detected: {duplicated_ids}')
        return 1

    null_summary = df[list(REQUIRED_COLUMNS)].isna().sum().sort_values(ascending=False)

    print('[OK] Dataset schema validated')
    print(f'[INFO] Rows: {len(df):,}')
    print(f'[INFO] Columns: {len(df.columns)}')
    print('[INFO] Null values by required column:')
    for column, count in null_summary.items():
        print(f'  - {column}: {int(count)}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

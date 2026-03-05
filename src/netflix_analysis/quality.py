from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "show_id",
    "title",
    "type",
    "director",
    "cast",
    "country",
    "date_added",
    "release_year",
    "duration",
    "genre",
    "description",
}


@dataclass
class ValidationResult:
    ok: bool
    rows: int
    columns: int
    duplicated_ids: int
    missing_columns: set[str]
    null_summary: dict[str, int]


def validate_dataset(path: Path) -> ValidationResult:
    if not path.exists():
        raise FileNotFoundError(f"Missing dataset: {path}")

    df = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    duplicated_ids = int(df["show_id"].duplicated().sum()) if "show_id" in df.columns else 0

    null_summary = (
        df[list(REQUIRED_COLUMNS & set(df.columns))]
        .isna()
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    ok = not missing_columns and duplicated_ids == 0
    return ValidationResult(
        ok=ok,
        rows=len(df),
        columns=len(df.columns),
        duplicated_ids=duplicated_ids,
        missing_columns=missing_columns,
        null_summary={k: int(v) for k, v in null_summary.items()},
    )

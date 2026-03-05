from pathlib import Path

import pandas as pd

from netflix_analysis.quality import validate_dataset


COLUMNS = [
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
]


def _write_csv(path: Path, rows: list[dict]):
    df = pd.DataFrame(rows, columns=COLUMNS)
    df.to_csv(path, index=False)


def test_validate_dataset_success(tmp_path: Path):
    csv_path = tmp_path / "ok.csv"
    _write_csv(
        csv_path,
        [
            {
                "show_id": "s1",
                "title": "Movie A",
                "type": "Movie",
                "director": "A",
                "cast": "A",
                "country": "US",
                "date_added": "2021-01-01",
                "release_year": 2020,
                "duration": "90 min",
                "genre": "Drama",
                "description": "desc",
            }
        ],
    )

    result = validate_dataset(csv_path)
    assert result.ok is True
    assert result.duplicated_ids == 0
    assert not result.missing_columns


def test_validate_dataset_duplicate_ids(tmp_path: Path):
    csv_path = tmp_path / "dupe.csv"
    row = {
        "show_id": "s1",
        "title": "Movie A",
        "type": "Movie",
        "director": "A",
        "cast": "A",
        "country": "US",
        "date_added": "2021-01-01",
        "release_year": 2020,
        "duration": "90 min",
        "genre": "Drama",
        "description": "desc",
    }
    _write_csv(csv_path, [row, row])

    result = validate_dataset(csv_path)
    assert result.ok is False
    assert result.duplicated_ids == 1

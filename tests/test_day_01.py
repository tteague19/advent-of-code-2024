"""Implements tests for the code for Day 1 of the Advent of Code."""

import os
from pathlib import Path

from click.testing import CliRunner
from dotenv import load_dotenv
import pytest

from src.cli.days.day_01 import (
    DATA_COL_NAMES,
    calculate_total_distance,
    day_01,
    load_input,
)

DATA_DIR = Path(__file__).parents[1] / "data" / "day_01"
DATA_FILE_PATH = DATA_DIR / "distances.csv"
INVALID_DATA_COL_NAMES_FILE_PATH = DATA_DIR / "invalid-col-names.csv"
INVALID_DATA_FILE_TYPE_FILE_PATH = DATA_DIR / "invalid-file-type.txt"
INVALID_DATA_TYPES_FILE_PATH = DATA_DIR / "invalid-data-types.csv"

load_dotenv()


def test_day_01_with_valid_input():
    """Test for Day 1 with valid input."""
    runner = CliRunner()
    result = runner.invoke(day_01, [DATA_FILE_PATH.as_posix()])
    assert result.exit_code == 0
    assert "Day 1: Not yet implemented" in result.output


def test_load_input_with_invalid_column_names():
    """Test for Day 1 with invalid column names in the input data."""

    with pytest.raises(AssertionError):
        load_input(file_path=INVALID_DATA_COL_NAMES_FILE_PATH)


def test_load_input_with_invalid_data_file_type():
    """Test for Day 1 with an invalid file type for the input data."""

    with pytest.raises(AssertionError):
        load_input(file_path=INVALID_DATA_FILE_TYPE_FILE_PATH)


def test_load_input_with_invalid_data_types():
    """Test for Day 1 with invalid data types in the input data."""

    with pytest.raises(AssertionError):
        load_input(file_path=INVALID_DATA_TYPES_FILE_PATH)


def test_load_input_with_valid_data():
    """Test for Day 1 with valid data."""
    data_frame = load_input(file_path=DATA_FILE_PATH)

    assert data_frame.shape[1] == len(DATA_COL_NAMES)


def test_calculate_total_distance():
    """Test for the calculate_total_distance function."""
    data_frame = load_input(file_path=DATA_FILE_PATH)
    result = calculate_total_distance(data_frame=data_frame)

    assert result == int(os.getenv("DAY_01_TOTAL_DISTANCE"))

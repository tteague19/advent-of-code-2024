"""
Implements a CLI that runs the exercise for Day 1 of the Advent of Code 2024.

The problem description can be found at: https://adventofcode.com/2024/day/1
"""

from pathlib import Path
import polars as pl
import click


DATA_COL_NAMES = {"left", "right"}
DATA_TYPE_ERROR_MESSAGE = " ".join(
    ["The input data in column {col_name}", "is not of the expected type."]
)
COLUMN_NAME_ERROR_MESSAGE = " ".join(
    [
        "The input data frame does not have the expected column names.",
        "Expected: {expected}",
    ]
)
FILE_TYPE_ERROR_MESSAGE = " ".join(
    [
        "The input data file is not of the expected type.",
        "Expected: .csv but received {file_type}.",
    ]
)


def validate_input_data_file_type(input_file_path: Path) -> None:
    """
    Validate the file type of the input data for this day's exercise.

    :param input_file_path: The path to the input file for this day's exercise.
    :type input_file_path: Path
    :raises AssertionError: If the input file is not of the expected type.
    """
    error_message = FILE_TYPE_ERROR_MESSAGE.format(
        file_type=input_file_path.suffix
    )
    assert input_file_path.suffix == ".csv", error_message


def validate_column_data_types(data_frame: pl.DataFrame) -> None:
    """
    Validate the data types in each column in the input data frame.

    :param data_frame: The input data for this day's exercise.
    :type data_frame: pl.DataFrame
    :raises AssertionError: If at least one of the columns in the input
        data frame does not contain data of the expected type.
    """
    for col_name in DATA_COL_NAMES:
        error_message = DATA_TYPE_ERROR_MESSAGE.format(col_name=col_name)
        assert data_frame[col_name].dtype == pl.Int64, error_message


def validate_column_names(data_frame: pl.DataFrame) -> None:
    """
    Validate the column names in the input data frame.

    :param data_frame: The input data for this day's exercise.
    :type data_frame: pl.DataFrame
    :raises AssertionError: If the input data frame does not have the expected
        column names.
    """
    column_names = set(data_frame.columns)
    error_message = COLUMN_NAME_ERROR_MESSAGE.format(expected=DATA_COL_NAMES)
    assert column_names == DATA_COL_NAMES, error_message


def load_input(file_path: Path) -> pl.DataFrame:
    """
    Load the input data for this day's exercise.

    :param file_path: The path to the input file for this day's exercise.
    :type file_path: Path
    :return: The input data for this day's exercise in a data frame with two
        columns: "left" and "right", each of which contain an integer in each
        row.
    :rtype: pl.DataFrame
    """
    validate_input_data_file_type(file_path)
    data_frame = pl.read_csv(file_path)

    validate_column_names(data_frame)
    validate_column_data_types(data_frame)

    return data_frame


def calculate_total_distance(data_frame: pl.DataFrame) -> int:
    """
    Calculate the total distance between the points in the input data.

    :param data_frame: The input data for this day's exercise.
    :type data_frame: pl.DataFrame
    :return: The total distance between the points in the input data as defined
        by the exercise.
    :rtype: int
    """
    return int(
        data_frame
        .with_columns(
            pl.col("left").sort().alias("left_sorted"),
            pl.col("right").sort().alias("right_sorted"),
        )
        .with_columns(
            pl.col("left_sorted")
            .sub(pl.col("right_sorted"))
            .abs()
            .alias("distance"),
        )
        .select("distance")
        .to_series()
        .sum()
    )


@click.command()
@click.argument(
    "input_file_path",
    type=click.Path(exists=True, readable=True, path_type=Path),
)
def day_01(input_file_path: Path) -> None:
    """
    Compute the solution for Day 1 of the Advent of Code 2024.

    :param input_file_path: The path to the input file for this day's exercise.
    :type input_file_path: Path
    """
    click.echo("Day 1: Not yet implemented")

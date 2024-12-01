"""Implements tests for the code for Day 1 of the Advent of Code."""

from click.testing import CliRunner

from src.cli.days.day_01 import day_01


def test_day_01():
    """Test for Day 1."""
    runner = CliRunner()
    result = runner.invoke(day_01)
    assert result.exit_code == 0
    assert "Day 1: Not yet implemented" in result.output

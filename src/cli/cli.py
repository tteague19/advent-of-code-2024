"""Implements the entry point for the command line interface."""

import click

from cli.days.day_01 import day_01


@click.group()
def cli():
    """A command line interface."""


@cli.command()
def hello():
    """Prints a greeting."""
    click.echo("Happy Holidays, World!")


cli.add_command(hello)
cli.add_command(day_01)


def main():
    """Entry point for the command line interface."""
    cli()


if __name__ == "__main__":
    main()

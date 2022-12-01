import click
import day1.day1 as day1


@click.command()
@click.option(
    "--day", type=click.IntRange(1, 25), default=1, help="Day of the month"
)
@click.option(
    "--part", type=click.IntRange(1, 2), default=1, help="Part of the day"
)
@click.option(
    "--input",
    type=click.Choice(["example", "personal"]),
    default="example",
    help="Input file",
)
def main(day, part, input):
    """Run the solution for the given day and part."""
    if day == 1:
        day1.main(part, input)


if __name__ == "__main__":
    main()

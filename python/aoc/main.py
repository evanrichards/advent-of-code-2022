import click
import pyperclip
import day1.day1 as day1
from colorama import Fore, Style


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
    click.echo(f"Day {day}, part {part}, input {input}")
    if day == 1:
        result = day1.main(part, input)
    else:
        raise NotImplementedError(f"Day {day} not implemented yet")
    pyperclip.copy(result)
    click.echo(
        f'{Fore.GREEN}Result{Style.RESET_ALL}: {Style.DIM}"{Style.RESET_ALL}{ result }{Style.DIM}" (Copied to clipboard){Style.RESET_ALL}'
    )


if __name__ == "__main__":
    main()

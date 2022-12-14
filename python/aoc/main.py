import click
import day1.day1 as day1
import day2.day2 as day2
import day3.day3 as day3
import day4.day4 as day4
import day5.day5 as day5
import day6.day6 as day6
import day7.day7 as day7
import day8.day8 as day8
import pyperclip
from colorama import Fore, Style


@click.command()
@click.option("--day", type=click.IntRange(1, 25), default=1, help="Day of the month")
@click.option("--part", type=click.IntRange(1, 2), default=1, help="Part of the day")
@click.option(
    "--input",
    type=click.Choice(["example", "personal"]),
    default="example",
    help="Input file",
)
def main(day: int, part: int, input: str) -> None:
    click.echo(f"Day {day}, part {part}, input {input}")
    if day == 1:
        result = day1.main(part, input)
    elif day == 2:
        result = day2.main(part, input)
    elif day == 3:
        result = day3.main(part, input)
    elif day == 4:
        result = day4.main(part, input)
    elif day == 5:
        result = day5.main(part, input)
    elif day == 6:
        result = day6.main(part, input)
    elif day == 7:
        result = day7.main(part, input)
    elif day == 8:
        result = day8.main(part, input)
    else:
        raise NotImplementedError(f"Day {day} not implemented yet")
    pyperclip.copy(result)
    click.echo(
        f'{Fore.GREEN}Result{Style.RESET_ALL}: {Style.DIM}"{Style.RESET_ALL}{ result }{Style.DIM}" (Copied to clipboard){Style.RESET_ALL}'
    )


if __name__ == "__main__":
    main()

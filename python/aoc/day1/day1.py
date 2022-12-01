from read_input_common import read_input_common


def read_day_input(input):
    return read_input_common(1, input)


def main(part, input):
    raw_data = read_day_input(input)
    per_elf = raw_data.split("\n\n")
    per_elf_totals = map(parse_elf_total, per_elf)
    if part == 1:
        return max(per_elf_totals)
    if part == 2:
        most_elf = sorted(per_elf_totals, reverse=True)
        return sum(most_elf[:3])


def parse_elf_total(elf):
    return sum(map(int, elf.split()))

def read_input_common(day: int, input: str) -> str:
    with open(f"aoc/day{day}/input/{input}.dat") as f:
        return f.read()

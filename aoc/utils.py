from aoc.const import INPUT_ROOT


def read_input(day: str) -> list[str]:
    """Read the input for the given day."""
    with open(INPUT_ROOT / f"day{day}.txt") as f:
        return f.readlines()

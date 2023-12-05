from aoc.const import INPUT_ROOT
from typing import Sequence


def read_input(day: str) -> list[str]:
    """Read the input for the given day."""
    with open(INPUT_ROOT / f"day{day}.txt") as f:
        return f.readlines()


def group[T](iterable: Sequence[tuple[str, T]], keys: tuple[str]) -> dict[str, T]:
    groups = {key: 0 for key in keys}

    for key, value in iterable:
        groups[key] += value

    return groups

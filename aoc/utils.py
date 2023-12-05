from aoc.const import INPUT_ROOT
from typing import Sequence
from aoc._types import Matrix


def read_input(day: str) -> list[str]:
    """Read the input for the given day."""
    with open(INPUT_ROOT / f"day{day}.txt") as f:
        return f.readlines()


def read_matrix(day: str) -> Matrix:
    """Read the input for the given day as a matrix."""
    return [list(line.strip()) for line in read_input(day)]

def group[T](iterable: Sequence[tuple[str, T]], keys: tuple[str]) -> dict[str, T]:
    groups = {key: 0 for key in keys}

    for key, value in iterable:
        groups[key] += value

    return groups

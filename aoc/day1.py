import re

from aoc.utils import read_input

DIGIT_MAP = {str(i): str(i) for i in range(1, 10)}


def numerics_from_sent(sent: str, digit_map: dict[str, str] | None = None) -> list[tuple[int, str]]:
    digit_map = digit_map or DIGIT_MAP

    ints = []
    for word, digit in digit_map.items():
        for occ in re.finditer(word, sent):
            ints.append((occ.start(), digit))

    return ints


def combine_first_last(numbers: list[tuple[int, str]]) -> int:
    if len(numbers) < 2:
        numbers = numbers * 2

    numbers.sort()
    ints = [i[1] for i in numbers]
    first, last = ints[0], ints[-1]

    return int(f"{first}{last}")


def part1(day_input: list[str]) -> int:
    sum = 0
    for line in day_input:
        ints = numerics_from_sent(line)
        sum += combine_first_last(ints)

    return sum


def part2(day_input: list[str]) -> int:
    string_number_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    sum = 0
    for line in day_input:
        ints = numerics_from_sent(line, digit_map={
            **DIGIT_MAP,
            **string_number_map,
        })
        sum += combine_first_last(ints)

    return sum


if __name__ == '__main__':
    day_input = read_input('01')
    print(f"{part1(day_input)=}")
    print(f"{part2(day_input)=}")

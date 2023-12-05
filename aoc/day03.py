import math
from typing import Sequence

from aoc._types import Matrix
from aoc.utils import read_matrix

SYMBOLS = (
    '%',
    '#',
    '*',
    '$',
    '/',
    '-',
    '&',
    '+',
    '@',
    '=',
)

type Coordinate = tuple[int, int]


def find_neighbors(input: Matrix, coord: Coordinate, symbols: Sequence[str]) -> tuple[Coordinate]:
    x, y = coord

    neighbors = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue

            try:
                if input[x + i][y + j] in symbols:
                    neighbors.add((x + i, y + j))
            except IndexError:
                continue

    for i, j in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        try:
            if input[x + i][y + j] in symbols:
                neighbors.add((x + i, y + j))
        except IndexError:
            continue

    return tuple(neighbors)


def touches(input: Matrix, coord: Coordinate, symbols: Sequence[str]) -> bool:
    return len(find_neighbors(input, coord, symbols)) > 0


def find_start(input: Matrix, coord: Coordinate) -> Coordinate:
    row = input[coord[0]]

    start = coord
    for y in range(coord[1], -1, -1):
        if not row[y].isnumeric():
            break

        start = (coord[0], y)

    return start


def find_end(input: Matrix, coord: Coordinate) -> Coordinate:
    row = input[coord[0]]

    end = coord
    for y in range(coord[1], len(row)):
        if not row[y].isnumeric():
            break

        end = (coord[0], y)

    return end


def read_number(input: Matrix, coord_range: tuple[Coordinate, ...]) -> int:
    number = ''

    start_y, end_y = coord_range[0][1], coord_range[1][1]
    for y in range(start_y, end_y + 1):
        number += input[coord_range[0][0]][y]

    return int(number)


def part1(input: Matrix) -> int:
    result = 0

    seen = set()
    for x, row in enumerate(input):
        for y, char in enumerate(row):
            if not char.isnumeric():
                continue

            if not touches(input, (x, y), SYMBOLS):
                continue

            coord = (x, y)
            coord_range = find_start(input, coord), find_end(input, coord)
            if coord_range in seen:
                continue

            start, end = coord_range
            result += read_number(input, (start, end))
            seen.add(coord_range)

    return result


def part2(input: Matrix) -> int:
    result = 0

    numeric_symbols = tuple(str(i) for i in range(10))
    seen = set()
    for x, row in enumerate(input):
        for y, char in enumerate(row):
            if char != '*':
                continue

            neighbors = find_neighbors(input, (x, y), numeric_symbols)
            neighbor_numbers = []
            for neighbor in neighbors:
                coord_range = find_start(input, neighbor), find_end(input, neighbor)
                if coord_range in seen:
                    continue

                start, end = coord_range
                neighbor_numbers.append(read_number(input, (start, end)))
                seen.add(coord_range)

            if len(neighbor_numbers) != 2:
                continue

            result += math.prod(neighbor_numbers)

    return result


if __name__ == '__main__':
    day_input = read_matrix('03')
    print(f"{part1(day_input)=}")
    print(f"{part2(day_input)=}")

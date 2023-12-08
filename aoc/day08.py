import itertools

from aoc.utils import read_input


def make_directions_and_map(day_input: list[str]) -> tuple[list[str], dict[str, list[str]]]:
    directions = list(day_input[0])

    map = {}
    for line in day_input[2:]:
        start, instructions = line.split(' = ')
        map[start] = instructions.replace('(', '').replace(')', '').split(', ')

    return directions, map


def part1(day_input: list[str]) -> int:
    steps = 0

    directions, map = make_directions_and_map(day_input)
    current = 'AAA'
    for instruction in itertools.cycle(directions):
        steps += 1
        if instruction == 'L':
            current = map[current][0]
        elif instruction == 'R':
            current = map[current][1]

        if current == 'ZZZ':
            break

    return steps


def part2(day_input: list[str]) -> int:
    steps = 0

    directions, map = make_directions_and_map(day_input)
    currents = [pos for pos in map.keys() if pos.endswith('A')]
    for instruction in itertools.cycle(directions):
        steps += 1
        idx = 0 if instruction == 'L' else 1
        currents = [map[current][idx] for current in currents]

        if all(current.endswith('Z') for current in currents):
            break

        if any(current.endswith('Z') for current in currents):
            print(f'{steps=}')

    return steps


if __name__ == '__main__':
    day_input = read_input('08')

    print(f"{part1(day_input)=}")
    print(f"{part2(day_input)=}")

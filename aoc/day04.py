import functools
import math

from aoc.utils import read_input


@functools.cache
def parse_game_set(line: str) -> tuple[int, set[int, ...], set[int, ...]]:
    card, cards = line.split(': ')
    _, card_id = card.rsplit(' ', 1)

    winning, mine = cards.split(' | ')

    return int(card_id), set(int(card) for card in winning.split()), set(int(card) for card in mine.strip().split())


def calculate_wins(line: str) -> int:
    _, winning, mine = parse_game_set(line)

    return len(winning.intersection(mine))


def part1(input: list[str]) -> int:
    result = 0
    for line in input:
        win_count = calculate_wins(line)
        if win_count == 0:
            continue

        result += int(math.pow(2, win_count - 1))
    return result


def part2(input: list[str]) -> int:
    result = 0

    multipliers = {}
    for line in input:
        card_id = parse_game_set(line)[0]

        multipliers[card_id] = 1

    for line in input:
        card_id, winning, mine = parse_game_set(line)
        copies = len(winning.intersection(mine))
        if copies == 0:
            continue

        for copy in range(card_id + 1, card_id + copies + 1):
            multipliers[copy] += multipliers[card_id]

    return sum(multipliers.values())


if __name__ == '__main__':
    day_input = read_input('04')
    print(f"{part1(day_input)=}")
    print(f"{part2(day_input)=}")

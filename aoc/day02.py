import math
from aoc.utils import read_input, group

MAX_COLORS_PER_ROUND = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def parse_round(round_string: str) -> list[tuple[int, str]]:
    rounds = []
    for cubes in round_string.split(','):
        count, color = cubes.strip().split(' ')
        rounds.append((color.strip(), int(count)))

    return rounds


def parse_rounds(rounds_string: str) -> list[list[tuple[int, str]]]:
    rounds = []
    for round_string in rounds_string.split(';'):
        rounds.append(parse_round(round_string))

    return rounds


def check(group: dict[str, int], max_counts: dict[str, int]) -> bool:
    for color, count in group.items():
        if count > max_counts[color]:
            return False

    return True


def game_possible(rounds: list[list[tuple[int, str]]], max_counts: dict[str, int]) -> bool:
    for round in rounds:
        round_group = group(round, keys=tuple(max_counts.keys()))
        if not check(round_group, max_counts):
            return False

    return True


def part1(input: list[str]) -> int:
    game_id_sum = 0
    for line in input:
        line = line.strip()
        game, rounds_string = line.split(': ')
        _, game_id = game.split(' ')

        rounds = parse_rounds(rounds_string)
        if not game_possible(rounds, MAX_COLORS_PER_ROUND):
            continue

        game_id_sum += int(game_id)

    return game_id_sum


def part2(input: list[str]) -> int:
    result = 0

    for line in input:
        line = line.strip()
        game, rounds_string = line.split(': ')
        _, game_id = game.split(' ')

        rounds = parse_rounds(rounds_string)
        mins = None
        for round_ in rounds:
            round_group = group(round_, keys=tuple(MAX_COLORS_PER_ROUND.keys()))
            if mins is None:
                mins = round_group

                continue

            for color, count in round_group.items():
                if count > mins[color] or mins[color] == 0:
                    mins[color] = count

        result += math.prod(mins.values())

    return result


if __name__ == '__main__':
    day_input = read_input('02')
    print(f"{part1(day_input)=}")
    print(f"{part2(day_input)=}")

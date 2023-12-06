import collections
import itertools

from aoc.utils import read_input

type Map = dict[str, list[int]]


def make_map(input: list[str]) -> Map:
    maps = collections.defaultdict(list)

    map_name = None
    for line in input:
        if not line:
            continue

        if line.endswith('map:'):
            map_name = line.strip().split(' ')[0]

            continue

        maps[map_name].append([int(i) for i in line.split(' ')])  # todo: parse line

    return maps


def part1(seeds: list[int], seed_map: Map) -> int:
    locations = []
    for seed in seeds:
        current_map = seed
        for i in seed_map.values():
            for j in i:
                if j[1] <= current_map < j[1] + j[2]:
                    current_map = j[0] + (current_map - j[1])

                    break
        locations.append(current_map)

    return min(locations)


def part2(seeds: list[int], seed_map: Map) -> int:

    return 0


if __name__ == '__main__':
    day_input = read_input('05')
    _, seeds = day_input[0].split(':')
    seeds = [int(seed) for seed in seeds.strip().split(' ')]
    map = make_map(day_input[2:])  # skip seeds and new line

    print(f"{part1(seeds, map)=}")
    print(f"{part2(seeds, map)=}")

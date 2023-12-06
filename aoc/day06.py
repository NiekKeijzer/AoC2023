import math

from aoc.utils import read_input


def parse(line: str) -> tuple[int]:
    line = line.split(':')[1].strip()
    return tuple(int(i) for i in line.split(' ') if i)


def part1(day_input: list[tuple[int, int]]) -> int:
    options = []
    for race_duration, distance in day_input:
        option_count = 0
        for charge_time in range(race_duration):
            option = (race_duration - charge_time) * charge_time

            if option > distance:
                option_count += 1

        options.append(option_count)

    return math.prod(options)


def part2(race_duration, distance) -> int:
    option_count = 0
    for charge_time in range(race_duration):
        option = (race_duration - charge_time) * charge_time

        if option > distance:
            option_count += 1

    return option_count


if __name__ == '__main__':
    day_input = read_input('06')
    times = parse(day_input[0])
    distance = parse(day_input[1])

    print(f"{part1(zip(times, distance))=}")

    time =int(''.join(str(d) for d in times))
    distance = int(''.join(str(d) for d in distance))
    print(f"{part2(time, distance)=}")

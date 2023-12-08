import collections
import functools

from aoc.utils import read_input

CARDS = (
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
)

type Hand = tuple[str, str, str, str, str]


def score_joker_hand(hand: Hand) -> int:
    scores = []
    _hand = list(hand)
    for i, card in enumerate(hand):
        if card != "J":
            continue

        for c in CARDS:
            if c == "J":
                continue

            _hand[i] = c
            if 'J' in _hand:
                scores.append(score_joker_hand(tuple(_hand)))
            else:
                scores.append(score_hand(tuple(_hand)))

    return max(scores)


def score_hand(hand: Hand) -> int:
    counts = {}

    for card in set(hand):
        counts[card] = hand.count(card)

    if len(counts) == 5:
        # High card
        return 1

    if len(counts) == 4:
        # One pair
        return 2

    if len(counts) == 3:
        if 3 in counts.values():
            # Three of a kind
            return 4
        else:
            # Two pair
            return 3

    if len(counts) == 2:
        if 4 in counts.values():
            # Four of a kind
            return 8
        else:
            # Full house
            return 7

    if len(counts) == 1:
        # Five of a kind
        return 9


@functools.cache
def parse_cards_bid(line: str) -> tuple[Hand, int]:
    cards, bid = line.split(' ')

    return tuple(list(cards)), int(bid)


def translate_hand(hand: Hand, joker: bool = False) -> tuple[int, ...]:
    if joker:
        cards = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')
    else:
        cards = CARDS

    return tuple(cards.index(c) for c in hand)


def part1(day_input: list[str]) -> int:
    groups = collections.defaultdict(list)

    for line in day_input:
        hand, bid = parse_cards_bid(line)
        score = score_hand(hand)

        groups[score].append((hand, bid))

    ranks = []
    for score in sorted(groups.keys()):
        groups[score].sort(key=lambda r: translate_hand(r[0]))

        ranks.extend(r[1] for r in groups[score])

    result = 0
    for rank, score in enumerate(ranks):
        result += score * (rank + 1)

    return result


def part2(day_input: list[str]) -> int:
    groups = collections.defaultdict(list)

    for line in day_input:
        hand, bid = parse_cards_bid(line)
        if 'J' in hand:
            score = score_joker_hand(hand)
        else:
            score = score_hand(hand)

        groups[score].append((hand, bid))

    ranks = []
    for score in sorted(groups.keys()):
        groups[score].sort(key=lambda r: translate_hand(r[0], joker=True))

        ranks.extend(r[1] for r in groups[score])

    result = 0
    for rank, score in enumerate(ranks):
        result += score * (rank + 1)

    return result


if __name__ == '__main__':
    score_hand(('T', '5', '5', 'J', '5'))
    day_input = read_input('07')

    print(f"{part1(day_input)=}")
    print(f"{part2(day_input)=}")

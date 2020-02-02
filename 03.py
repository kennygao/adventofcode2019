import re
from enum import Enum, auto
from typing import NamedTuple, Sequence, Tuple

from kennygao.functions import compose


class Direction(Enum):
    D = auto()
    L = auto()
    R = auto()
    U = auto()


class Step(NamedTuple):
    direction: Direction
    distance: int


WirePath = Sequence[Step]


def main():
    part1 = compose(
            load_puzzle_input,
            lambda x: map(parse_wire_path, x),
            list,
    )('03.txt')
    print(f'{part1=}')


def load_puzzle_input(file_path: str) -> Tuple[str, str]:
    with open(file_path) as f:
        puzzle_input = f.read()
    first, second, *ignored = puzzle_input.splitlines()
    return first, second


def parse_wire_path(wire_path_description: str) -> WirePath:
    def parse_step(step_description: str) -> Step:
        direction, distance = re.fullmatch(r'([DLRU])(\d+)', step_description).groups()
        return Step(Direction[direction], distance)

    return [parse_step(step_description) for step_description in wire_path_description.split(',')]


if __name__ == '__main__':
    main()

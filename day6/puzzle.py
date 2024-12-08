from __future__ import annotations
from dataclasses import dataclass
from typing import Generator, Iterable


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, vec: Vector) -> Vector:
        return Vector(self.x + vec.x, self.y + vec.y)


Grid = dict[Vector, str]


def read_input() -> tuple[Grid, Vector]:
    grid: dict[Vector, str] = {}
    start_pos = Vector(0, 0)
    with open("input.txt") as f:
        for y, row in enumerate(f.readlines()):
            for x, col in enumerate(row.strip()):
                pos = Vector(int(x), int(y))
                if col == "^":
                    start_pos = pos
                    grid[pos] = "."
                else:
                    grid[pos] = col
    return grid, start_pos


def turn() -> Generator[Vector, None, None]:
    while True:
        yield Vector(0, -1)
        yield Vector(1, 0)
        yield Vector(0, 1)
        yield Vector(-1, 0)


def part1(grid: Grid, pos: Vector) -> int:
    visited: set[Vector] = set()
    next_direction = turn()
    direction = next(next_direction)
    while pos in grid:
        visited.add(pos)
        next_pos = pos + direction
        if next_pos not in grid:
            break
        if grid[next_pos] == "#":
            direction = next(next_direction)
        else:
            pos = next_pos
    return len(visited)


def part2(grid: Grid, guard: Vector) -> int:
    return 0


def solve() -> None:
    grid, guard = read_input()

    result1 = part1(grid, guard)
    print(f"Part 1: {result1}")

    result2 = part2(grid, guard)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

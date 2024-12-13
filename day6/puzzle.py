from __future__ import annotations
from dataclasses import dataclass
from typing import Generator


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


def part1(grid: Grid, guard: Vector) -> set[Vector]:
    path: set[Vector] = set()
    next_direction = turn()
    direction = next(next_direction)
    while guard in grid:
        path.add(guard)
        next_position = guard + direction
        if next_position not in grid:
            break
        if grid[next_position] == "#":
            direction = next(next_direction)
        else:
            guard = next_position
    return path


def part2(
    grid: Grid,
    guard: Vector,
    original_path: set[Vector],
) -> int:
    loops = 0

    for possible_position in grid:
        if (
            grid[possible_position] != "."
            or possible_position not in original_path
            or possible_position == guard
        ):
            continue

        path: set[tuple[Vector, Vector]] = set()
        next_direction = turn()
        direction = next(next_direction)
        position = guard
        while position in grid:
            if (position, direction) in path:
                loops += 1
                break
            path.add((position, direction))
            next_position = position + direction
            if next_position not in grid:
                break
            if grid[next_position] == "#" or next_position == possible_position:
                direction = next(next_direction)
            else:
                position = next_position
    return loops


def solve() -> None:
    grid, guard = read_input()

    visited = part1(grid, guard)
    print(f"Part 1: {len(visited)}")

    result2 = part2(grid, guard, visited)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

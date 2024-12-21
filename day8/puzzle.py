from __future__ import annotations
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __mul__(self, other: int) -> Vector:
        return Vector(self.x * other, self.y * other)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)


@dataclass(frozen=True)
class Antenna:
    pos: Vector
    frequency: str


Grid = dict[Vector, str]
Antennas = dict[str, set[Antenna]]


def read_input() -> tuple[Grid, Antennas]:
    grid: Grid = {}
    antennas: Antennas = defaultdict(set)
    with open("input.txt") as f:
        for y, row in enumerate(f.readlines()):
            for x, col in enumerate(row.strip()):
                if col != ".":
                    antennas[col].add(Antenna(Vector(x, y), col))
                grid[Vector(x, y)] = col
    return (grid, antennas)


def part_1(grid: Grid, antennas_by_frequency: Antennas) -> int:
    for antennas in antennas_by_frequency.values():
        for antenna in antennas:
            for other in antennas:
                if other == antenna:
                    continue
                antinode = antenna.pos + (antenna.pos - other.pos)
                if antinode in grid and grid[antinode] != "#":
                    grid[antinode] = "#"
    return len([tile for tile in grid.values() if tile == "#"])


def part2(grid: Grid, antennas_by_frequency: Antennas) -> int:
    for antennas in antennas_by_frequency.values():
        for antenna in antennas:
            for other in antennas:
                if other == antenna:
                    continue
                multiplier = 0
                antinode = antenna.pos + (antenna.pos - other.pos) * multiplier
                while antinode in grid:
                    if grid[antinode] != "#":
                        grid[antinode] = "#"
                    multiplier += 1
                    antinode = antenna.pos + (antenna.pos - other.pos) * multiplier
    return len([tile for tile in grid.values() if tile == "#"])


def solve() -> None:
    grid, antennas = read_input()

    result1 = part_1(deepcopy(grid), antennas)
    print(f"Part 1: {result1}")

    result2 = part2(deepcopy(grid), antennas)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

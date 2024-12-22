from __future__ import annotations
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, other: Vector):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector):
        return Vector(self.x - other.x, self.y - other.y)


Grid = dict[Vector, int]


def read_input() -> Grid:
    grid = {}
    with open("input.txt") as f:
        for y, row in enumerate(f.readlines()):
            for x, col in enumerate(row.strip()):
                grid[Vector(x, y)] = int(col)
    return grid


def count_trails(grid: Grid, distinct_only: bool) -> int:
    trailheads = [(vec, height) for vec, height in grid.items() if height == 0]

    score = 0
    for trailhead in trailheads:
        queue = deque([trailhead])
        visited = set()
        while queue:
            pos, height = queue.popleft()
            if height == 9 and pos not in visited:
                score += 1
                if distinct_only:
                    visited.add(pos)
                continue
            visited.add(pos)
            for vec in [Vector(1, 0), Vector(0, 1), Vector(-1, 0), Vector(0, -1)]:
                next = pos + vec
                if next not in visited and grid.get(next) == height + 1:
                    queue.append((next, height + 1))
    return score


def part1(grid: Grid) -> int:
    return count_trails(grid, True)


def part2(grid: Grid) -> int:
    return count_trails(grid, False)


def solve() -> None:
    grid = read_input()

    result1 = part1(grid)
    print(f"Part 1: {result1}")

    result2 = part2(grid)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

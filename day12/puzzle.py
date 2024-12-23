from __future__ import annotations
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int) -> Vector:
        return Vector(self.x * other, self.y * other)


Grid = dict[Vector, str]


def read_input() -> Grid:
    grid: Grid = {}
    with open("input.txt") as f:
        for y, row in enumerate(f):
            for x, plant in enumerate(row.strip()):
                grid[Vector(x, y)] = plant
    return grid


def bfs(grid: Grid, plant: str, start: Vector) -> set[Vector]:
    visited: set[Vector] = set()
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        for vec in [Vector(1, 0), Vector(0, 1), Vector(-1, 0), Vector(0, -1)]:
            next = pos + vec
            if grid.get(next) == plant and next not in visited:
                queue.append(next)
    return visited


def perimeter(area: set[Vector]) -> int:
    count = 0
    for pos in area:
        for vec in [Vector(1, 0), Vector(0, 1), Vector(-1, 0), Vector(0, -1)]:
            if pos + vec not in area:
                count += 1
    return count


def part1(grid: Grid) -> int:
    visited: set[Vector] = set()
    areas: dict[str, set[Vector]] = {}
    for pos, plant in grid.items():
        if pos in visited:
            continue
        area = bfs(grid, plant, pos)
        visited.update(area)
        areas[f"{plant}-{len(areas) + 1}"] = area

    return sum(len(area) * perimeter(area) for area in areas.values())


corner_patterns = set(
    [
        # Outside corners
        "....AA.AA",
        "...AA.AA.",
        ".AA.AA...",
        "AA.AA....",
        # Inside corners
        "AAAAAAAA.",
        "AAAAAA.AA",
        ".AAAAAAAA",
        "AA.AAAAAA",
        # Edge cases from example
        "A...AA.AA",
        "..AAA.AA.",
        ".AA.AAA..",
        "AA.AA...A",
    ]
)


def is_corner(pos: Vector, area: set[Vector]) -> bool:
    pattern = ""
    for offset in [
        Vector(-1, -1),
        Vector(0, -1),
        Vector(1, -1),
        Vector(-1, 0),
        Vector(0, 0),
        Vector(1, 0),
        Vector(-1, 1),
        Vector(0, 1),
        Vector(1, 1),
    ]:
        pattern += "A" if (pos + offset) in area else "."
    return pattern in corner_patterns


def part2(grid: Grid) -> int:
    visited: set[Vector] = set()
    areas: dict[str, set[Vector]] = {}
    for pos, plant in grid.items():
        if pos in visited:
            continue
        area = bfs(grid, plant, pos)
        visited.update(area)
        areas[f"{plant}-{len(areas) + 1}"] = area

    total = 0
    for plant, area in areas.items():
        upscaled = set()
        for vector in area:
            for x in range(0, 3):
                for y in range(0, 3):
                    upscaled.add(vector * 3 + Vector(x, y))
        corners = [vec for vec in upscaled if is_corner(vec, upscaled)]
        total += len(area) * len(corners)
    return total


def solve() -> None:
    grid = read_input()

    result1 = part1(grid)
    print(f"Part 1: {result1}")

    result2 = part2(grid)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

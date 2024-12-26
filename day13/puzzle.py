from __future__ import annotations
import functools
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, other) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)


@dataclass(frozen=True)
class Machine:
    a: Vector
    b: Vector
    prize: Vector


def read_input() -> list[Machine]:
    machines = []
    with open("input.txt") as f:
        for group in f.read().split("\n\n"):
            ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", group))
            machines.append(Machine(Vector(ax, ay), Vector(bx, by), Vector(px, py)))
    return machines


@functools.cache
def dfs(position: Vector, tokens: tuple[int, int], machine: Machine) -> int:
    if position == machine.prize:
        return sum(tokens)

    results = [1024]
    if tokens[0] < 300:
        results.append(dfs(position + machine.a, (tokens[0] + 3, tokens[1]), machine))
    if tokens[1] < 100:
        results.append(dfs(position + machine.b, (tokens[0], tokens[1] + 1), machine))
    return min(results)


def part1(machines: list[Machine]) -> int:
    total = 0
    for machine in machines:
        cost = dfs(Vector(0, 0), (0, 0), machine)
        if cost != 1024:
            total += cost
    return total


def part2(machines: list[Machine]) -> int:
    total = 0
    for machine in machines:
        scaled_prize_x = machine.prize.y + 10000000000000
        scaled_prize_y = machine.prize.x + 10000000000000
        b = (scaled_prize_x * machine.a.x - machine.a.y * scaled_prize_y) / (
            machine.b.y * machine.a.x - machine.a.y * machine.b.x
        )
        a = (scaled_prize_y - machine.b.x * b) / machine.a.x
        if a.is_integer() and b.is_integer():
            total += 3 * int(a) + int(b)
    return total


def solve() -> None:
    machines = read_input()

    result1 = part1(machines)
    print(f"Part 1: {result1}")

    result2 = part2(machines)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

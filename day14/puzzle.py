from __future__ import annotations
from collections import deque
from copy import deepcopy
from functools import reduce
from operator import mul
import re
from dataclasses import dataclass


HEIGHT = 103
WIDTH = 101


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)


@dataclass
class Robot:
    pos: Vector
    vel: Vector

    def move(self) -> None:
        self.pos += self.vel


def read_input() -> list[Robot]:
    robots = []
    with open("input.txt") as f:
        for line in f.readlines():
            px, py, vx, vy = re.findall(r"-?\d+", line)
            robots.append(Robot(Vector(int(px), int(py)), Vector(int(vx), int(vy))))
    return robots


def part1(robots: list[Robot]) -> int:
    turns = 100
    while turns > 0:
        for robot in robots:
            robot.move()
            robot.pos = Vector(robot.pos.x % WIDTH, robot.pos.y % HEIGHT)
        turns -= 1

    quadrants = [0, 0, 0, 0]
    horizontal_split = WIDTH // 2
    vertical_split = HEIGHT // 2
    for robot in robots:
        robot.pos = Vector(robot.pos.x % WIDTH, robot.pos.y % HEIGHT)
        if robot.pos.x != horizontal_split and robot.pos.y != vertical_split:
            if robot.pos.x < horizontal_split:
                quadrants[0 if robot.pos.y < vertical_split else 2] += 1
            else:
                quadrants[1 if robot.pos.y < vertical_split else 3] += 1
    return reduce(mul, quadrants)


def part2(robots: list[Robot]) -> int:
    turn = 1
    while True:
        robot_positions = set()
        for robot in robots:
            robot.move()
            robot.pos = Vector(robot.pos.x % WIDTH, robot.pos.y % HEIGHT)
            robot_positions.add(robot.pos)
        visited = set()
        area_sizes = []
        for robot in robot_positions:
            if robot in visited:
                continue
            area_size = 0
            queue = deque([robot])
            while queue:
                pos = queue.popleft()
                area_size += 1
                visited.add(pos)
                for vector in [
                    Vector(0, 1),
                    Vector(1, 0),
                    Vector(-1, 0),
                    Vector(0, -1),
                ]:
                    next_pos = pos + vector
                    if next_pos in robot_positions and next_pos not in visited:
                        queue.append(next_pos)
            area_sizes.append(area_size)
        if max(area_sizes) > 20:
            break
        turn += 1
    return turn


def solve() -> None:
    robots = read_input()

    result1 = part1(deepcopy(robots))
    print(f"Part 1: {result1}")

    result2 = part2(deepcopy(robots))
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

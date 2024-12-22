from __future__ import annotations
from collections import defaultdict


def read_input() -> list[int]:
    with open("input.txt") as f:
        return [int(stone) for stone in f.read().split()]


def blink(stones: list[int], blinks: int) -> int:
    prev_gen = defaultdict(int)
    for stone in stones:
        prev_gen[stone] += 1

    while blinks > 0:
        next_gen = defaultdict(int)
        for stone, count in prev_gen.items():
            if stone == 0:
                next_gen[1] += count
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                left = int(stone_str[: len(stone_str) // 2])
                right = int(stone_str[len(stone_str) // 2 :])
                next_gen[left] += count
                next_gen[right] += count
            else:
                next_gen[stone * 2024] += count
        prev_gen = next_gen
        blinks -= 1

    return sum(stone for stone in prev_gen.values())


def part1(stones: list[int]) -> int:
    return blink(stones, 25)


def part2(stones: list[int]) -> int:
    return blink(stones, 75)


def solve() -> None:
    stones = read_input()

    result1 = part1(stones)
    print(f"Part 1: {result1}")

    result2 = part2(stones)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

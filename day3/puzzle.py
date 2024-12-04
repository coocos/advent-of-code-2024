import re


def read_input() -> str:
    with open("input.txt") as f:
        return f.read().replace("\n", "").strip()


def part1(memory: str) -> int:
    pattern = r"mul\((\d+),(\d+)\)"
    return sum(int(x) * int(y) for x, y in re.findall(pattern, memory))


def part2(memory: str) -> int:
    pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    total = 0
    enabled = True
    for x, y, do, dont in re.findall(pattern, memory):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif x and y and enabled:
            total += int(x) * int(y)
    return total


def solve() -> None:
    memory = read_input()

    result1 = part1(memory)
    print(f"Part 1: {result1}")

    result2 = part2(memory)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

from collections import Counter


def read_input() -> list[list[int]]:
    """Read and parse input from input.txt"""
    a = []
    b = []
    with open("input.txt") as f:
        for line in f.readlines():
            x, y = line.split()
            a.append(int(x))
            b.append(int(y))
    return [a, b]


def part1(a: list[int], b: list[int]) -> int:
    """Solve part 1 of the puzzle"""
    return sum(abs(p1 - p2) for p1, p2 in zip(sorted(a), sorted(b)))


def part2(a: list[int], b: list[int]) -> int:
    """Solve part 2 of the puzzle"""
    counts = Counter(b)
    return sum(n * counts.get(n, 0) for n in a)


def solve() -> None:
    """Solve both parts of the puzzle"""
    a, b = read_input()

    result1 = part1(a, b)
    print(f"Part 1: {result1}")

    result2 = part2(a, b)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

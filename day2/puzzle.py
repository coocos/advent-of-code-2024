from typing import Iterable


def read_input() -> list[list[int]]:
    """Read and parse input from input.txt"""
    reports = []
    with open("input.txt") as f:
        for line in f.readlines():
            report = [int(x) for x in line.strip().split()]
            reports.append(report)
    return reports


def is_safe(report: list[int]) -> bool:
    for level in range(1, len(report) - 1):
        left = report[level - 1] - report[level]
        right = report[level] - report[level + 1]
        if (left < 0 and right > 0) or (left > 0 and right < 0):
            return False
        if abs(left) > 3 or abs(left) < 1 or abs(right) > 3 or abs(right) < 1:
            return False
    return True


def variations(report: list[int]) -> Iterable[list[int]]:
    for level in range(len(report)):
        yield report[:level] + report[level + 1 :]


def part1(reports: list[list[int]]) -> int:
    """Solve part 1 of the puzzle"""
    return sum(1 for report in reports if is_safe(report))


def part2(reports: list[list[int]]) -> int:
    """Solve part 2 of the puzzle"""
    return sum(
        1
        for report in reports
        if is_safe(report) or any(is_safe(v) for v in variations(report))
    )


def solve() -> None:
    """Solve both parts of the puzzle"""
    data = read_input()

    result1 = part1(data)
    print(f"Part 1: {result1}")

    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

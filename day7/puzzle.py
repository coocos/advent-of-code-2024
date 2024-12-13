from typing import Iterable


Equation = tuple[int, list[int]]


def read_input() -> list[Equation]:
    equations: list[Equation] = []
    with open("input.txt") as f:
        for line in f.readlines():
            left, right = line.split(":")
            result = int(left)
            numbers = [int(number.strip()) for number in right.split()]
            equations.append((result, numbers))
    return equations


def combinations(numbers: list[int], total: int, concat: bool) -> Iterable[int]:
    head, *tail = numbers
    if not tail:
        yield total * head
        yield total + head
        if concat:
            yield int(f"{total}{head}")
        return
    yield from combinations(tail, total + head, concat)
    yield from combinations(tail, total * head, concat)
    if concat:
        yield from combinations(tail, int(f"{total}{head}"), concat)


def calibrate(equations: list[Equation], concat: bool) -> int:
    calibration_result = 0
    for value, numbers in equations:
        for combination in combinations(numbers[1:], numbers[0], concat):
            if combination == value:
                calibration_result += value
                break
    return calibration_result


def part1(equations: list[Equation]) -> int:
    return calibrate(equations, False)


def part2(equations: list[Equation]) -> int:
    return calibrate(equations, True)


def solve() -> None:
    equations = read_input()

    result1 = part1(equations)
    print(f"Part 1: {result1}")

    result2 = part2(equations)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

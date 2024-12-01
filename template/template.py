def read_input():
    """Read and parse input from input.txt"""
    data = []
    with open("input.txt") as f:
        for line in f.readlines():
            # Parse input according to puzzle needs
            pass
    return data


def part1(data) -> int:
    """Solve part 1 of the puzzle"""
    return 0


def part2(data) -> int:
    """Solve part 2 of the puzzle"""
    return 0


def solve() -> None:
    """Solve both parts of the puzzle"""
    data = read_input()

    result1 = part1(data)
    print(f"Part 1: {result1}")

    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

def read_input():
    data = []
    with open("input.txt") as f:
        for line in f.readlines():
            pass
    return data


def part1(data) -> int:
    return 0


def part2(data) -> int:
    return 0


def solve() -> None:
    data = read_input()

    result1 = part1(data)
    print(f"Part 1: {result1}")

    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

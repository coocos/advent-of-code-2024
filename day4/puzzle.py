Grid = list[list[str]]


def read_input() -> Grid:
    grid = []
    with open("input.txt") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid


def gather(grid: Grid, y: int, x: int, dy: int, dx: int, depth: int = 3) -> str:
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid) or depth < 0:
        return ""
    return grid[y][x] + gather(grid, y + dy, x + dx, dy, dx, depth - 1)


def part1(grid: Grid) -> int:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            for dy, dx in directions:
                if gather(grid, y, x, dy, dx) == "XMAS":
                    count += 1
    return count


def part2(grid: Grid) -> int:
    count = 0
    words = {"MAS", "SAM"}
    for y in range(len(grid)):
        for x in range(len(grid) - 2):
            left = gather(grid, y, x, 1, 1, 2)
            right = gather(grid, y, x + 2, 1, -1, 2)
            if left in words and right in words:
                count += 1
    return count


def solve() -> None:
    grid = read_input()

    result1 = part1(grid)
    print(f"Part 1: {result1}")

    result2 = part2(grid)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

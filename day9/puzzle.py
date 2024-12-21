from copy import deepcopy


def read_input() -> list[int | None]:
    blocks: list[int | None] = []
    with open("input.txt") as f:
        file_id = 0
        for i, digit in enumerate(f.read().strip()):
            if i % 2 == 0:
                blocks += [file_id] * int(digit)
                file_id += 1
            else:
                blocks += [None] * int(digit)
    return blocks


def part1(blocks: list[int | None]) -> int:
    left = 0
    right = len(blocks) - 1
    while left != right:
        if blocks[left] is None and blocks[right] is not None:
            blocks[left] = blocks[right]
            blocks[right] = None
            left += 1
            right -= 1
        elif blocks[left] is not None:
            left += 1
        elif blocks[right] is None:
            right -= 1

    return sum(pos * int(file_id) for pos, file_id in enumerate(blocks) if file_id)


def part2(blocks: list[int | None]) -> int:
    file_id = max(block for block in blocks if block is not None)
    while file_id != 0:
        reversed_blocks = blocks[::-1]
        file_end = reversed_blocks.index(file_id)
        file_start = file_end
        while reversed_blocks[file_start] == file_id:
            file_start += 1
        file_start = len(blocks) - file_start
        file_size = len(blocks) - file_end - file_start

        space_start = 0
        while space_start != file_start:
            if (
                blocks[space_start] is None
                and len(set(blocks[space_start : space_start + file_size])) == 1
            ):
                break
            space_start += 1

        if space_start and space_start != file_start:
            blocks[space_start : space_start + file_size] = [file_id] * file_size
            blocks[file_start : file_start + file_size] = [None] * file_size
        file_id -= 1

    return sum(pos * file_id for pos, file_id in enumerate(blocks) if file_id)


def solve() -> None:
    blocks = read_input()

    result = part1(deepcopy(blocks))
    print(f"Part 1: {result}")

    result2 = part2(deepcopy(blocks))
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

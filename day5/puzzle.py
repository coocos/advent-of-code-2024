from collections import defaultdict

Rules = dict[int, set[int]]
Updates = list[list[int]]


def read_input() -> tuple[Rules, Updates]:
    rules: Rules = defaultdict(set)
    updates: Updates = []
    with open("input.txt") as f:
        raw_rules, raw_updates = f.read().split("\n\n")
        for rule in raw_rules.split("\n"):
            a, b = rule.split("|")
            rules[int(b)].add((int(a)))
        for update in raw_updates.split("\n"):
            updates.append([int(page) for page in update.split(",")])
    return rules, updates


def split(rules: Rules, updates: Updates) -> tuple[Updates, Updates]:
    valid = []
    invalid = []
    for update in updates:
        is_valid = True
        processed_pages = set()
        for page in update:
            required_pages = rules[page].intersection(set(update))
            if required_pages and not required_pages.issubset(processed_pages):
                is_valid = False
                break
            processed_pages.add(page)
        (valid if is_valid else invalid).append(update)
    return valid, invalid


def part1(rules: Rules, updates: Updates) -> int:
    valid_updates, _ = split(rules, updates)
    return sum(update[len(update) // 2] for update in valid_updates)


def part2(rules: Rules, updates: Updates) -> int:
    _, invalid_updates = split(rules, updates)

    middle_pages = 0
    for update in invalid_updates:
        scoped_rules = {
            page: rule.intersection(set(update))
            for page, rule in rules.items()
            if page in update
        }
        valid_update = [
            page
            for page, _ in sorted(
                scoped_rules.items(),
                key=lambda page_rules: len(page_rules[1]),
            )
        ]
        middle_pages += valid_update[len(valid_update) // 2]
    return middle_pages


def solve() -> None:
    rules, updates = read_input()

    result1 = part1(rules, updates)
    print(f"Part 1: {result1}")

    result2 = part2(rules, updates)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    solve()

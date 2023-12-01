nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def hasNumber(line: str, index: int, allowText=False, reverse=False) -> None or int:
    if line[index].isnumeric():
        return line[index]

    elif allowText:
        for key, val in nums.items():
            sub = line[: index + 1] if not reverse else line[index:]
            if key in sub:
                return val

    return None


def part1() -> int:
    f = open("input/day1.txt", "r")
    data = f.read().splitlines()
    f.close()

    nums = list()
    for line in data:
        first, last, c = None, None, 0
        while not first:
            first = hasNumber(line, c)
            c += 1

        c = -1
        while not last:
            last = hasNumber(line, c, reverse=True)
            c -= 1

        number = int(f"{first}{last}")
        nums.append(number)

    return sum(nums)


def part2() -> int:
    f = open("input/day1.txt", "r")
    data = f.read().splitlines()
    f.close()

    nums = list()
    for line in data:
        first, last, c = None, None, 0
        while not first:
            first = hasNumber(line, c, allowText=True)
            c += 1

        c = -1
        while not last:
            last = hasNumber(line, c, allowText=True, reverse=True)
            c -= 1

        number = int(f"{first}{last}")
        nums.append(number)

    return sum(nums)


if __name__ == "__main__":
    print(part1())
    print(part2())

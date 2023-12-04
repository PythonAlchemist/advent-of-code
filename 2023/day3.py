def buildNumber(line: str, j: int) -> int:
    num = ""
    while j < len(line) and line[j].isnumeric():
        num += line[j]
        j += 1

    return int(num)


def checkMap(lines: list[str], i: int, j: int) -> bool:
    search = [
        (i - 1, j),
        (i, j + 1),
        (i + 1, j),
        (i, j - 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j + 1),
        (i + 1, j - 1),
    ]
    for x, y in search:
        if x < 0 or y < 0:
            continue
        elif x > len(lines) - 1 or y > len(lines[x]) - 1:
            continue
        elif lines[x][y] != "." and not lines[x][y].isnumeric():
            return True
    return False


def searchNum(lines: list[str], i: int, j: int) -> None or int:
    search = [
        (i - 1, j),
        (i, j + 1),
        (i + 1, j),
        (i, j - 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j + 1),
        (i + 1, j - 1),
    ]
    nums = list()
    seen = set()
    for x, y in search:
        if x < 0 or y < 0:
            continue
        elif x > len(lines) - 1 or y > len(lines[x]) - 1:
            continue
        elif lines[x][y].isnumeric():
            offset = 0
            temp = lines[x][y - offset]
            while temp.isnumeric():
                offset += 1
                temp = lines[x][y - offset]
            offset -= 1

            if num := buildNumber(lines[x], y - offset):
                if (x, y - offset) not in seen:
                    seen.add((x, y - offset))
                    nums.append(num)

    if len(nums) == 2:
        return nums[0] * nums[1]

    return None


def part1(data: list[str]) -> int:
    parts = list()
    seen = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isnumeric() and (i, j) not in seen:
                num = buildNumber(data[i], j)
                for z in range(len(str(num))):
                    seen.add((i, j + z))

                if any([checkMap(data, i, j + z) for z in range(len(str(num)))]):
                    parts.append(num)

    return sum(parts)


def part2(data: list[str]) -> int:
    parts = list()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "*":
                if val := searchNum(data, i, j):
                    parts.append(val)

    return sum(parts)


if __name__ == "__main__":
    f = open("input/day3.txt")
    lines = f.read().splitlines()
    f.close()

    print(part1(lines))
    print(part2(lines))

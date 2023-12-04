from collections import defaultdict


def gamePossible(game: dict, constraints: dict) -> bool:
    for i in range(len(game)):
        for color, num in game[i].items():
            if color in constraints:
                if num > constraints[color]:
                    return False
    return True


def minPossible(game: dict) -> dict:
    maxx = defaultdict(int)
    for i in range(len(game)):
        for color, num in game[i].items():
            if num > maxx[color]:
                maxx[color] = num

    # calculate power
    power = 1
    for color, num in maxx.items():
        power *= num

    return power


def gameRecord() -> dict:
    f = open("input/day2.txt", "r")
    data = f.read().splitlines()
    f.close()

    game = dict()
    for line in data:
        game_id, record = line.split(":")
        game_num = int(game_id.split(" ")[1])
        game[game_num] = dict()
        sets = record.split(";")
        for i, s in enumerate(sets):
            game[game_num][i] = defaultdict(int)
            entries = s.split(",")
            for entry in entries:
                num, color = entry.strip().split(" ")
                num = int(num.strip())
                color = color.strip()
                game[game_num][i][color] = num

    return game


def part1() -> int:
    games = gameRecord()
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    sum = 0
    for game_id, game in games.items():
        if gamePossible(game, constraints):
            sum += game_id

    return sum


def part2() -> int:
    games = gameRecord()
    sum = 0
    for game_id, game in games.items():
        sum += minPossible(game)

    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())

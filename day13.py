from itertools import combinations
from collections import defaultdict

data = open("./inputs/day13.txt").read().splitlines()


def parse(data) -> list:
    # return list of pairs of elements
    pairs = list()
    q = False
    for i, line in enumerate(data):
        if line == "":
            q = False
            continue

        if not q:
            pairs.append((eval(line), eval(data[i + 1])))
            q = True

    return pairs


def compare(l, r):

    # both are ints
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        elif l > r:
            return False
        elif l == r:
            return None

    # both are lists
    elif isinstance(l, list) and isinstance(r, list):
        length = max(len(l), len(r))
        for j in range(length):
            if j >= len(r):
                return False
            elif j >= len(l):
                return True
            else:
                val = compare(l[j], r[j])
                if val == True:
                    return True
                elif val == False:
                    return False
                elif val == None:
                    continue

    # one is list, one is int
    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    else:
        print("ERROR")
        return None


# part 1
pairs = parse(data)

correct = list()
for i in range(len(pairs)):

    l = pairs[i][0]
    r = pairs[i][1]
    if compare(l, r) == True:
        correct.append(i + 1)

print(f"Part 1: {sum(correct)}")

# part 2

# flatten list
signal = [pair[0] for pair in pairs] + [pair[1] for pair in pairs]
signal.append([[2]])
signal.append([[6]])

# create pairs of indices to compare
pair_combos = list(combinations(range(len(signal)), 2))


# determinte which indicies can come before which
order = defaultdict(list)
for i in range(len(pair_combos)):

    l = signal[pair_combos[i][0]]
    r = signal[pair_combos[i][1]]

    if compare(l, r) == True:
        order[pair_combos[i][0]].append(pair_combos[i][1])
    elif compare(l, r) == False:
        order[pair_combos[i][1]].append(pair_combos[i][0])
    else:
        print("ERROR")

# order of signal indices based on number of indicies that can come after it
order = sorted(order, key=lambda x: len(order[x]), reverse=True)

# find decoder index
decoder = list()
for i in range(len(order)):
    if signal[order[i]] == [[2]]:
        decoder.append(i + 1)
    elif signal[order[i]] == [[6]]:
        decoder.append(i + 1)

print(f"Part 2: {decoder[0] * decoder[1]}")

import numpy as np

data = open("./inputs/day14.txt").read().splitlines()


def addSand(grid, part):

    # starts at origin
    pos = (0, 500)

    # keep moving until we hit the bottom
    movement = True
    while movement:

        if grid[pos[0] + 1, pos[1]] == ".":
            pos = (pos[0] + 1, pos[1])
        elif grid[pos[0] + 1, pos[1] - 1] == ".":
            pos = (pos[0] + 1, pos[1] - 1)
        elif grid[pos[0] + 1, pos[1] + 1] == ".":
            pos = (pos[0] + 1, pos[1] + 1)
        else:
            movement = False

        # escape condition - defined by part
        # part 1 - stop at bottom
        if part == 1:
            if pos[0] == len(grid) - 1:
                return None
        # part 2 - stop at origin
        if part == 2:
            if pos == (0, 500):
                return None

    # index sand resting place
    return pos


def parsePoitnt(p1, p2):
    p1 = p1.split(",")
    p2 = p2.split(",")
    p1 = (int(p1[1]), int(p1[0]))
    p2 = (int(p2[1]), int(p2[0]))

    return (p1, p2)


# convert data to list of endpoints pairs
endpoints = list()
for line in data:
    instructions = line.split(" -> ")
    for i in range(1, len(instructions)):
        endpoints.append(parsePoitnt(instructions[i - 1], instructions[i]))


# zero out grid
grid = np.zeros((1000, 1000), dtype=str)
grid[:, :] = "."

# convert endpoints to paths, const4ruct grid
for p1, p2 in endpoints:

    # horizontal paths
    if p1[0] == p2[0]:
        row, c1, c2 = p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])
        grid[row, c1 : c2 + 1] = "#"
    # vertical paths
    elif p1[1] == p2[1]:
        col, r1, r2 = p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])
        grid[r1 : r2 + 1, col] = "#"
    else:
        print("ERROR")

### part 1 - pouring sand

grid_copy = grid.copy()

ct = 0
while True:
    pos = addSand(grid_copy, 1)
    if pos == None:
        break
    else:
        grid_copy[pos[0], pos[1]] = "o"
        ct += 1

print(f"Part 1: {ct}")

###  part 2 - covering origin
# find the lowest row in grid
low = 0
for i in range(len(grid)):
    if "#" in grid[i, :]:
        low = i


# modify grid to include floor: truncate and add floor
grid2 = grid[0 : low + 3, :]
grid2[low + 2, :] = "#"

ct = 0
while True:
    pos = addSand(grid2, 2)
    if pos == None:
        break
    else:
        grid2[pos[0], pos[1]] = "o"
        ct += 1

# Add 1 to account for the origin
print(f"Part 2: {ct+1}")

def tailMech(head, tail) -> list:

    row_lead = head[0] - tail[0]
    col_lead = head[1] - tail[1]

    # if tail is 1 away from head, don't move the tail
    # this can be in line or diagonal
    if -1 <= row_lead <= 1 and -1 <= col_lead <= 1:
        return tail

    # handle inline movement
    elif row_lead > 1 and col_lead == 0:
        return [tail[0] + 1, tail[1]]
    elif row_lead < -1 and col_lead == 0:
        return [tail[0] - 1, tail[1]]
    elif row_lead == 0 and col_lead > 1:
        return [tail[0], tail[1] + 1]
    elif row_lead == 0 and col_lead < -1:
        return [tail[0], tail[1] - 1]

    # handle diagonal movement
    # both equal to 1 or -1 will be handled by the first if case
    elif row_lead >= 1 and col_lead >= 1:
        return [tail[0] + 1, tail[1] + 1]
    elif row_lead >= 1 and col_lead <= -1:
        return [tail[0] + 1, tail[1] - 1]
    elif row_lead <= -1 and col_lead >= 1:
        return [tail[0] - 1, tail[1] + 1]
    elif row_lead <= -1 and col_lead <= -1:
        return [tail[0] - 1, tail[1] - 1]
    else:
        print("I missed a case")
        print("head: ", head)
        print("tail: ", tail)
        return tail


# parse movement of head knot
data = open("./inputs/day9.txt", "r").read().splitlines()

# dictionary of head movement
headMove = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

### part 1 - count visited squares by the tail

# initialize visited matrix
visited = [[False for i in range(1000)] for j in range(1000)]

head = [0, 0]
tail = [0, 0]

for line in data:
    dir = line[0]
    dist = int(line[1:])

    # move head knot for each step in direction
    # this will also move the tail knot if needed for each sub step
    for i in range(dist):
        head[0] += headMove[dir][0]
        head[1] += headMove[dir][1]

        tail = tailMech(head, tail)
        visited[tail[0]][tail[1]] = True

total = sum([i.count(True) for i in visited])
print(f"Part 1: {total}")

### part 2 - count visited squares by the 9th knot

# initialize visited matrix
visited = [[False for i in range(1000)] for j in range(1000)]

# initialize knot dictionary
# key = knot number, 0 = head, 9 = tail
knots = {k: [0, 0] for k in range(10)}

for line in data:
    dir = line[0]
    dist = int(line[1:])

    # move head knot for each step in direction
    # this will also move the tail knot if needed for each sub step
    for i in range(dist):

        # knot 0 is the head
        knots[0][0] += headMove[dir][0]
        knots[0][1] += headMove[dir][1]

        # move knot k based on knot k-1, and current knot position
        for k in range(1, 10):
            knots[k] = tailMech(knots[k - 1], knots[k])

        # mark tail as visited (only the last knot is the tail)
        visited[knots[9][0]][knots[9][1]] = True

total = sum([i.count(True) for i in visited])
print(f"Part 2: {total}")

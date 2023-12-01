data = open("./inputs/day12.txt", "r").read().splitlines()

# capture grid values
grid = [[val for val in line.strip()] for line in data]

# find start and end positions
start, end = None, None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
            grid[i][j] = "a"
        elif grid[i][j] == "E":
            end = (i, j)
            grid[i][j] = "z"

# part 2 - find shortest path of mulitple paths
start_options = list()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "a":
            start_options.append((i, j))


# construct adjacency list
adj_list = dict()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        adj_list[(i, j)] = list()

        L, R, U, D = (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        # check for left edge exclusion
        if L[1] >= 0 and ord(grid[L[0]][L[1]]) - ord(grid[i][j]) <= 1:
            adj_list[(i, j)].append(L)

        # check for right edge exclusion
        if R[1] < len(grid[0]) and ord(grid[R[0]][R[1]]) - ord(grid[i][j]) <= 1:
            adj_list[(i, j)].append(R)

        # check for upper edge exclusion
        if U[0] >= 0 and ord(grid[U[0]][U[1]]) - ord(grid[i][j]) <= 1:
            adj_list[(i, j)].append(U)

        # check for lower edge exclusion
        if D[0] < len(grid) and ord(grid[D[0]][D[1]]) - ord(grid[i][j]) <= 1:
            adj_list[(i, j)].append(D)


def bfs(start, end):
    # find shortest path
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, dist = queue.pop(0)
        if node == end:
            return dist
        if node not in visited:
            visited.add(node)
            for neighbor in adj_list[node]:
                queue.append((neighbor, dist + 1))

    # if no path found, return a large number
    return 10e6


# part 1
a = bfs(start, end)
print(f"Part 1: {a}")

# part 2
dist_list = list()
for start in start_options:
    dist_list.append(bfs(start, end))
b = min(dist_list)
print(f"Part 2: {b}")

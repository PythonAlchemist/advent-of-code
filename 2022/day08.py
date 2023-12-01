import numpy as np

data = open("./inputs/day8.txt", "r").read().splitlines()
data = [list(line) for line in data]
matrix = np.matrix(data, dtype=int)

# part 1 - count visible trees

# initialize visible booleans and set edges to visible
visible = np.zeros(matrix.shape, dtype=bool)
visible[:, 0] = True
visible[0, :] = True
visible[-1, :] = True
visible[:, -1] = True

shape = matrix.shape

# skip edges
for i in range(1, shape[0] - 1):
    for j in range(1, shape[1] - 1):

        # skip if already visible
        if visible[i][j] is True:
            continue

        height = matrix[i, j]

        # check north
        if all(height > matrix[:i, j].flatten().tolist()[0]):
            visible[i, j] = True

        # check south
        if all(height > matrix[i + 1 :, j].flatten().tolist()[0]):
            visible[i, j] = True

        # check west
        if all(height > matrix[i, :j].tolist()[0]):
            visible[i, j] = True

        # check east
        if all(height > matrix[i, j + 1 :].tolist()[0]):
            visible[i, j] = True

print(sum(sum(visible)))

# part 2 - count nearby trees
def countNearby(list, height):

    # if on edge of forest, return 0
    if len(list) == 0:
        return 0

    count = 0
    for i in range(len(list)):
        # count the blocking tree then break
        if list[i] >= height:
            count += 1
            break
        else:
            count += 1
    return count


# initialize matrix of zeros
nearby = np.zeros(matrix.shape, dtype=int)

max_score = 0
shape = matrix.shape
for i in range(1, shape[0] - 1):
    for j in range(1, shape[1] - 1):

        height = matrix[i, j]

        s = countNearby(matrix[i + 1 :, j].flatten().tolist()[0], height)
        e = countNearby(matrix[i, j + 1 :].tolist()[0], height)

        # reverse the list to count from the other direction when counting up and left
        n = countNearby(matrix[:i, j].flatten().tolist()[0][::-1], height)
        w = countNearby(matrix[i, :j].tolist()[0][::-1], height)

        score = n * s * w * e
        if score > max_score:
            max_score = score

print(max_score)

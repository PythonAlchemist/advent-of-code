from collections import defaultdict
import numpy as np


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def generate_clouds(pairs, target):
    target_set = set()
    # convert pairs to clouds, construct column sets
    for sensor, beacon in pairs:
        sx, sy = sensor
        bx, by = beacon

        # calc distance
        dist = manhattan(sensor, beacon)

        d_target = abs(sy - target)
        width = abs(dist - d_target)
        mark = range(sx - width, sx + width + 1)

        target_set.update(mark)

    return target_set


data = open("./inputs/test.txt").read().splitlines()

# convert data to list of sensor, beacon pairs
pairs = list()
for line in data:
    sensor, beacon = line.split(":")
    s_x = sensor.split(",")[0].split("=")[1]
    s_y = sensor.split(",")[1].split("=")[1]
    b_x = beacon.split(",")[0].split("=")[1]
    b_y = beacon.split(",")[1].split("=")[1]
    pairs.append(((int(s_x), int(s_y)), (int(b_x), int(b_y))))


## part 1
target = 10
# target = 2000000

target_set = generate_clouds(pairs, target)


# reset sensor and beacon markers
for sensor, beacon in pairs:
    sx, sy = sensor
    bx, by = beacon

    # remove sensor and beacon from target set
    if sy == target and sx in target_set:
        target_set.remove(sx)
    if by == target and bx in target_set:
        target_set.remove(bx)

print(f"Part 1: {len(target_set)}")

## part 2

target_range = (0, 20)
# target_range = (0, 4000000)

full_range = set(range(*target_range))

for target in range(*target_range):
    target_set = generate_clouds(pairs, target)
    print(target)
    print(target_set)

    diff = full_range.difference(target_set)
    print(diff)
    if len(diff) != 0:
        print(diff)

# print(f"Part 2: {x*4000000 + y}")

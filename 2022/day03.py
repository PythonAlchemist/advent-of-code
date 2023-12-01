def contains_common(a, b, c):
    d1 = set(a)
    d2 = set(b)
    d3 = set(c)

    return list(d1 & d2 & d3)[0]


ct = 0
data = open("./inputs/day3.txt", "r").read().splitlines()
lines = list()
line_ct = 0
for line in data:
    lines.append(line)
    line_ct += 1

    if line_ct % 3 == 0:
        l1 = lines[0]
        l2 = lines[1]
        l3 = lines[2]
        lines = list()
        line_ct = 0

        com = contains_common(l1, l2, l3)

        if com.islower():
            ct += ord(com) - 96
        elif com.isupper():
            ct += ord(com) - 38

print(ct)

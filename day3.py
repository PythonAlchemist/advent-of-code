def contains_common(a, b, c):
    d1 = dict()
    d2 = dict()
    d3 = dict()
    for i in a:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in b:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    for i in c:
        if i in d3:
            d3[i] += 1
        else:
            d3[i] = 1

    return list(set(d1.keys()) & set(d2.keys()) & set(d3.keys()))[0]


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

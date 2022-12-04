def isOverlap(elf1, elf2) -> bool:

    e1_start = int(elf1.split("-")[0])
    e1_end = int(elf1.split("-")[1])
    e2_start = int(elf2.split("-")[0])
    e2_end = int(elf2.split("-")[1])

    e1 = set(range(e1_start, e1_end + 1))
    e2 = set(range(e2_start, e2_end + 1))

    return len(e1 & e2) > 0


data = open("./inputs/day4.txt", "r").read().splitlines()

ct = 0
for line in data:
    line = line.split(",")
    elf1 = line[0]
    elf2 = line[1]

    if isOverlap(elf1, elf2):
        ct += 1

print(ct)

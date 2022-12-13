mx = [0, 0, 0]
local = 0
data = open("./inputs/day1.txt").read().splitlines()
for line in data:
    if line != "":
        local += int(line)
    else:
        if local > mx[0]:
            mx[0] = local
        local = 0
        mx.sort()

print(mx)
print(sum(mx))

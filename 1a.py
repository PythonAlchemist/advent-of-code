mx = 0
local = 0
data = open("./inputs/1a.txt").read().splitlines()
for line in data:
    if line != "":
        local += int(line)
    else:
        if local > mx:
            mx = local
        local = 0

print(mx)

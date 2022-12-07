def changeDown(currDir, dirName):
    if currDir == "/":
        currDir += dirName
    else:
        currDir += f"/{dirName}"
    return currDir


def changeUp(currDir):
    currDir = currDir[: currDir.rfind("/")]
    if currDir == "":
        currDir = "/"
    return currDir


# store in a list of strings
data = open("./inputs/day7.txt", "r").read().splitlines()
data = [line for line in data]

# transform data into a list of lists
# 0th element is the command prompt
packets = list()
pack = list()
for line in data:
    if line[0] == "$" and len(pack) > 0:
        packets.append(pack)
        pack = list()
        pack.append(line)
    else:
        pack.append(line)
packets.append(pack)

currDir = "/"
dirs = dict()

for pack in packets[1:]:

    # command prompt
    command = pack[0].split()

    # change directory downward
    if command[1] == "cd" and command[2] != "..":
        currDir = changeDown(currDir, command[2])

    # change directory upward
    elif command[1] == "cd" and command[2] == "..":
        currDir = changeUp(currDir)

    if currDir not in dirs:
        dirs[currDir] = 0

    if command[1] == "ls":
        for payload in pack:
            payload = payload.split()
            if payload[0] == "dir":
                tempDir = changeDown(currDir, payload[1])
                if tempDir not in dirs:
                    dirs[tempDir] = 0
            elif payload[0].isnumeric():
                dirs[currDir] += int(payload[0])


# sort keys by name
dirs = dict(
    sorted(dirs.items(), key=lambda k: (len(k[0].split("/")), len(k[0])), reverse=True)
)

# roll up the tree
for k, v in dirs.items():
    if k != "/":
        parent = k[: k.rfind("/")]
        if parent == "":
            parent = "/"

        dirs[parent] += v


# part 1 - sum directories with less than 100,000 bytes
ct = 0
for k, v in dirs.items():
    if v <= 100_000:
        ct += v

print(ct)

# part 2 - free up the smallest space needed for update

diskSize = 70_000_000
spaceNeeded = 30_000_000
spaceFree = diskSize - dirs["/"]
toBeDeleted = spaceNeeded - spaceFree

# take smallest value from filtered dirs
dirs = {k: v for k, v in dirs.items() if v >= toBeDeleted}
dirs = dict(sorted(dirs.items(), key=lambda k: k[1]))
print(dirs[list(dirs.keys())[0]])

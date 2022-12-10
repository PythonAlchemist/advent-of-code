data = open("./inputs/day10.txt", "r").read().splitlines()

# dummy val at index 0
reg_list = [1]
for line in data:
    line = line.split()
    instruction = line[0]

    if instruction == "noop":
        # add 1 cycle of nothing
        reg_list.append(reg_list[-1])
    elif instruction == "addx":
        # add 1 cycles of nothing
        # add 1 cycle of add
        reg_list.append(reg_list[-1])
        reg_list.append(reg_list[-1] + int(line[1]))


# part 1 - sim elements of the register list

# initlaize count and index
ct, idx = 0, 20

# while within range of list ad 40 cycles
while True:
    if idx > len(reg_list):
        break
    else:
        ct += reg_list[idx - 1] * idx
    idx += 40

print(ct)

# part 2 - visualize the register list

output = []
for i in range(len(reg_list)):

    # find the spirit in horizontal position
    sprint_i = i % 40

    # find if spirit in register range
    if sprint_i - 1 <= reg_list[i] <= sprint_i + 1:
        output.append("#")
    else:
        output.append(".")

output = "".join(output)

# create vizualization
print(output[0:40])
print(output[40:80])
print(output[80:120])
print(output[120:160])
print(output[160:200])
print(output[200:240])

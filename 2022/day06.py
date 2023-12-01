data = open("./inputs/day6.txt", "r").read().splitlines()[0]

# starting marker size
window = 14

for i in range(len(data) - window):
    slice = data[i : i + window]
    if len(set(slice)) == len(list(slice)):
        print(i + window)
        break

from collections import defaultdict

data = open("./inputs/day5.txt", "r").read().splitlines()

d = defaultdict(list)

parse = True
for line in data:

    # read initial state of stacks
    if parse:
        size = len(line)
        for i in range(0, size):
            if line[i].isalpha():

                # access correct stack by character position
                d[1 + (i // 4)].append(line[i])

    # read moves after initial state
    else:
        print(d)
        op = line.split()
        num, fr, to = int(op[1]), int(op[3]), int(op[5])

        # move top n disks from stack fr to stack to

        # part 1
        # reverse order of disks with pop and append
        # [d[to].append(d[fr].pop()) for _ in range(num)]

        # part 2
        # move disks in order with extnd and slice
        d[to].extend(d[fr][-num:])
        d[fr] = d[fr][0:-num]

    # reverse stacks and change loop behavior
    if line == "":

        for k, v in d.items():
            d[k] = v[::-1]

        parse = False


result = ""
d = dict(sorted(d.items()))
for k, v in d.items():
    result += "".join(v[-1])

print(result)

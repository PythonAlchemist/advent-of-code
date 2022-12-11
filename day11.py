from math import gcd

data = open("./inputs/day11.txt", "r").read().splitlines()

# initialize monkey holding items
monkeys = dict()

# monkey index
m_i = None

for line in data:
    line = line.strip().split()

    # skip empty lines
    if len(line) == 0:
        continue

    elif line[0] == "Monkey":

        # initialize metadata for monkey
        m_i = int(line[1][0])
        monkeys[m_i] = dict()
        monkeys[m_i]["items"] = list()
        monkeys[m_i]["touches"] = 0
        monkeys[m_i]["oper"] = None
        monkeys[m_i]["test"] = None
        monkeys[m_i]["throw"] = [None, None]

    # starting items
    elif line[0] == "Starting":
        items = "".join(line[2:]).split(",")
        items = [monkeys[m_i]["items"].append(int(i)) for i in reversed(items)]

    # store operation in string for eval
    elif line[0] == "Operation:":
        func = "".join(line[3:])
        monkeys[m_i]["oper"] = func

    # modulus divisor
    elif line[0] == "Test:":
        monkeys[m_i]["test"] = int(line[3])

    elif line[0] == "If" and line[1] == "true:":
        monkeys[m_i]["throw"][0] = int(line[5])

    elif line[0] == "If" and line[1] == "false:":
        monkeys[m_i]["throw"][1] = int(line[5])

    else:
        print("I missed a case")

# run string eval
def inspect(k, old) -> int:
    return eval(monkeys[k]["oper"])


# determine which monkey to throw to
def toss(k, worry) -> int:

    if worry % monkeys[k]["test"] == 0:
        return monkeys[k]["throw"][0]
    else:
        return monkeys[k]["throw"][1]


def lcm(nums: list) -> int:
    lcm = 1
    for i in nums:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


factors = list()
for i in range(len(monkeys.keys())):
    factors.append(monkeys[i]["test"])

div_factor = lcm(factors)

# rounds of throwing
for i in range(10_000):

    if i % 10 == 0:
        print(f"Round {i} -> {i/10_000:.2%} Complete")

    # iterate through monkeys
    for j in range(0, len(monkeys.keys())):

        # reverse the stack to make it a queue
        monkeys[j]["items"] = monkeys[j]["items"][::-1]

        for worry in monkeys[j]["items"]:

            # iterate the number of touches
            monkeys[j]["touches"] += 1

            worry = inspect(j, worry)

            # part 1
            # worry = worry // 3

            # part 2
            worry %= div_factor

            new_monkey = toss(j, worry)
            monkeys[new_monkey]["items"].append(worry)

        # clear the items after thrown all of them
        monkeys[j]["items"] = list()


touch = list()
for i in range(len(monkeys.keys())):
    touch.append(monkeys[i]["touches"])
print(touch)


touch.sort(reverse=True)
print(touch[0] * touch[1])

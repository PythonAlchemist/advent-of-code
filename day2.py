# part 1
points = {
    "X": 1,  # A Rock
    "Y": 2,  # B Paper
    "Z": 3,  # C Scissors
}

winPoints = {
    ("X", "A"): 3,
    ("X", "B"): 0,
    ("X", "C"): 6,
    ("Y", "A"): 6,
    ("Y", "B"): 3,
    ("Y", "C"): 0,
    ("Z", "A"): 0,
    ("Z", "B"): 6,
    ("Z", "C"): 3,
}

# part 2

howToPlay = {
    ("X", "A"): "C",
    ("X", "B"): "A",
    ("X", "C"): "B",
    ("Y", "A"): "A",
    ("Y", "B"): "B",
    ("Y", "C"): "C",
    ("Z", "A"): "B",
    ("Z", "B"): "C",
    ("Z", "C"): "A",
}

winPoints = {
    # (win/lose/draw, shapeChoice)
    # lose - add 0
    ("X", "A"): 1,
    ("X", "B"): 2,
    ("X", "C"): 3,
    # draw - add 3
    ("Y", "A"): 4,
    ("Y", "B"): 5,
    ("Y", "C"): 6,
    # win - add 6
    ("Z", "A"): 7,
    ("Z", "B"): 8,
    ("Z", "C"): 9,
}


ct = 0
data = open("./inputs/day2.txt").read().splitlines()
for line in data:
    line = line.split()
    theyPlay = line[0]
    wld = line[1]
    Ichoose = howToPlay[(wld, theyPlay)]

    ct += winPoints[(wld, Ichoose)]

print(ct)

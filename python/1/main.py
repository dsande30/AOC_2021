import os


# Part 1
i = 0
prev = 0
with open(os.path.dirname(__file__) + '/input', 'r') as f:
    for current in f.readlines():
        if prev != 0 and prev < int(current):
            i += 1
        prev = int(current)

    print("Part 1: {}".format(i))


# Part 2
i = 0
window1 = [0, 0, 0]
window2 = [0, 0, 0]

with open(os.path.dirname(__file__) + '/input', 'r') as f:
    for index, current in enumerate(f.readlines()):
        if index < 3:
            continue
        window1[0] = window1[1]
        window1[1] = window1[2]
        window1[2] = window2[2]
        window2[0] = window2[1]
        window2[1] = window2[2]
        window2[2] = int(current)

        if sum(window1) < sum(window2):
            i += 1
    print("Part 2: {}".format(i))

import os

# Part 1
bits = [0] * 12
gamma = ["0"] * 12
epsilon = ["0"] * 12
with open(os.path.dirname(__file__) + '/input', 'r') as f:
    data = f.readlines()
    for line in data:
        for index, char in enumerate(line):
            if char == "1":
                bits[index] += 1
    for index, bit in enumerate(bits):
        if bit > len(data) / 2:
            gamma[index] = "1"
        else:
            epsilon[index] = "1"
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    print("Part 1: {}".format(gamma * epsilon))


# Part 2
# This code feels pretty sloppy, but I'm trying to focus on completion rather than quality.
o2 = []
co2 = []
with open(os.path.dirname(__file__) + '/input', 'r') as f:
    data = f.readlines()
    data = [row.strip() for row in data] # strip newlines
    data_transpose = [[row.strip()[i] for row in data]for i in range(len(data[0]) - 1)]
    o2 = data.copy()
    o2_copy = data.copy()
    for index in range(12):
        if len(o2) == 1:
            break
        o2_copy = o2.copy()
        row_transpose = [[row[i] for row in o2_copy]for i in range(len(o2_copy[0]))][index]
        most_common = "0" if row_transpose.count('0') > row_transpose.count('1') else "1"
        least_common = "1" if row_transpose.count('0') > row_transpose.count('1') else "0"
        tie = row_transpose.count('0') == row_transpose.count('1')
        for line in o2_copy:
            if line[index] == least_common or (tie == True and line[index] == "0"):
                o2.remove(line)

    co2 = data.copy()
    co2_copy = data.copy()
    for index in range(12):
        if len(co2) == 1:
            break
        co2_copy = co2.copy()
        row_transpose = [[row[i] for row in co2_copy]for i in range(len(co2_copy[0]))][index]
        most_common = "0" if row_transpose.count('0') > row_transpose.count('1') else "1"
        least_common = "1" if row_transpose.count('0') > row_transpose.count('1') else "0"
        tie = row_transpose.count('0') == row_transpose.count('1')
        for line in co2_copy:
            if line[index] == most_common or (tie == True and line[index] == "1"):
                co2.remove(line)
    print("Part 2: {}".format(int(o2[0], 2) * int(co2[0], 2)))


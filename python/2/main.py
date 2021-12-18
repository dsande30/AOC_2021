import os

# Part 1
depth = 0
horizontal = 0
with open(os.path.dirname(__file__) + '/input', 'r') as f:
    for line in f.readlines():
        command, val = line.split(' ')
        if command == "forward":
            horizontal += int(val)
        if command == "down":
            depth += int(val)
        if command == "up":
            depth -= int(val)
        
    print("Part 1: {}".format(horizontal * depth))

# Part 2
depth = 0
horizontal = 0
aim = 0
with open(os.path.dirname(__file__) + '/input', 'r') as f:
    for line in f.readlines():
        command, val = line.split(' ')
        if command == "forward":
            horizontal += int(val)
            depth += aim * int(val)
        if command == "down":
            aim += int(val)
        if command == "up":
            aim -= int(val)
    
    print("Part 2: {}".format(horizontal * depth))
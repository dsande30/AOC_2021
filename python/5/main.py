import os

# Part 1

# Some thoughts:
# It's late, but does x + 1 actually need to be x - 1 since this starts with 0,0 in the top left corner?
# I don't know, I'll look at it tomorrow.

class Line(object):
    x1 = None
    y1 = None
    x2 = None
    y2 = None

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.run = self.x2 - self.x1
        self.rise = self.y2 - self.y1

    def __str__(self):
        return "({},{}) -> ({},{})".format(self.x1, self.y1, self.x2, self.y2)

    def add_area_covered(self, board):
        if self.run < 0:
            for i in range(self.run):
                # print("Adding point at ({},{})".format(self.x1 - i, self.y1))
                board[self.x1 - i - 1][self.y1 - 1] += 1
        elif self.run > 0:
            for i in range(self.run):
                # print("Adding point at ({},{})".format(self.x1 + i, self.y1))
                board[self.x1 + i - 1][self.y1 - 1] += 1
        if self.rise < 0:
            for i in range(self.rise):
                # print("Adding point at ({},{})".format(self.x1, self.y1 - i))
                board[self.x1 - 1][self.y1 - i - 1] += 1
        elif self.rise > 0:
            for i in range(self.rise):
                # print("Adding point at ({},{})".format(self.x1, self.y1 + i))
                board[self.x1 - 1][self.y1 + i - 1] += 1
        return board


straight_lines = []
max_x = 0
max_y = 0
with open(os.path.dirname(__file__) + "/input", 'r') as f:
    for line in f.readlines():
        begin = line.split('->')[0].strip()
        x1 = int(begin.split(',')[0])
        y1 = int(begin.split(',')[1])
        end = line.split('->')[1].strip()
        x2 = int(end.split(',')[0])
        y2 = int(end.split(',')[1])
        line_segment = Line(x1, y1, x2, y2)
        if x1 > max_x:
            max_x = x1
        elif x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        elif y2 > max_y:
            max_y = y2
        
        if x1 == x2 or y1 == y2:
            straight_lines.append(line_segment)
        print("Beginning: ({},{})\tEnd: ({},{})".format(x1, y1, x2, y2))
    print("Max: ({},{})".format(max_x, max_y))

print("Number of straight lines: {}".format(len(straight_lines)))
board = [[0 for i in range(max_x)] for j in range(max_y)]

for line in straight_lines:
    board = line.add_area_covered(board)

count = 0
for i in range(max_x):
    for j in range(max_y):
        if board[i][j] > 1:
            count += 1
for row in board:
    print(row)
print(count)
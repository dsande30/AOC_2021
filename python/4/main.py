import os
from typing import final

# Part 1
# Part 2 is a slight modification at the end
def check_score(board, bingo_board, final_val):
    sum = 0
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if bingo_board[i][j] == False:
                sum += int(val)
    return sum * int(final_val)

def check_row(row):
    if False in row:
        return False
    else:
        return True

def check_col(rows, col_index):
    col = [row[col_index] for row in rows]
    if False in col:
        return False
    else:
        return True

def check_for_bingo(board, played_moves):
    l = len(board[0])
    w = len(board)
    bingo_board = [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]
    moves_played = []
    for move in played_moves:
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if move == val:
                    bingo_board[i][j] = True
        moves_played.append(move)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if check_row(bingo_board[i]) or check_col(bingo_board, j):
                    score = check_score(board, bingo_board, move)
                    return score, len(moves_played)


boards = []
moves = []
board = []
high_score = 0
low_score = 0
lowest_moves = 1000000000000 # large number
highest_moves = 0
with open(os.path.dirname(__file__) + "/input", 'r') as f:
    for index, line in enumerate(f.readlines()):
        if index == 0:
            line = line.strip().split(',')
            moves = line
        else:
            line = line.strip().split(' ')
            while line != [''] and '' in line:
                line.remove('')
        if index > 1 and line != ['']:
            board.append(list(line))
        if line == [''] and board != []:
            boards.append(board)
            board = []
    boards.append(board)
    for b in boards:
        score, num_moves = check_for_bingo(b, moves)
        if num_moves < lowest_moves:
            lowest_moves = num_moves
            high_score = score
        if num_moves > highest_moves:
            highest_moves = num_moves
            low_score = score
        elif num_moves == lowest_moves:
            print("TIED")
    print("Part 1: {}".format(high_score))
    print("Part 2: {}".format(low_score))
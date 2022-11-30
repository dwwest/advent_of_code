import numpy as np
import copy

""" LOAD DATA"""

boards = []
with open('input.txt', 'r') as f:
    for ind, line in enumerate(f):
        if ind == 0:
            numbers = [int(i) for i in line.split(',')]
        else:
            if line.strip('\n') != '':
                boards.append([int(i) for i in line.strip('\n').split()])

# make a numpy array of the boards
boards = np.reshape(np.array(boards), [int(len(np.ravel(boards))/25),5,5])
# make a numpy array to keep track of marks (1s) and nonmarks (0s)
marks = np.ones(np.shape(boards))

""" PART ONE """

board_num = None
for n in numbers:
    for board, mark in zip(boards, marks):
        for ind in np.argwhere(board==n):
            mark[ind[0],ind[1]] = 0.
    for mark_ind, mark in enumerate(marks):
        for rc in [mark, mark.T]:
            for row in rc:
                if 1. not in row:
                    board_num = mark_ind
                    just_called = n
                    break
            if board_num != None:
                break
        if board_num != None:
            break
    if board_num != None:
        break

board_sum = np.sum(boards[board_num]*marks[board_num])
print(board_sum*just_called)


""" PART TWO """

win_order = []
all_wins = False
marks = np.ones(np.shape(boards))
for n in numbers:
    for board, mark in zip(boards, marks):
        for ind in np.argwhere(board==n):
            mark[ind[0],ind[1]] = 0.
    for mark_ind, mark in enumerate(marks):
        if mark_ind in win_order:
            continue
        win = False
        for rc in [mark, mark.T]:
            for row in rc:
                if 1. not in row:
                    win_order.append(mark_ind)
                    just_called = n
                    win = True
                    if len(win_order) == np.shape(boards)[0]:
                        last_mark = copy.deepcopy(mark)
                    break
            if win == True:
                break
board_sum = np.sum(last_mark*boards[win_order[-1]])
print(board_sum*just_called)

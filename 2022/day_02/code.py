import numpy as np


""" IMPORT DATA """
with open('input.txt', 'r') as f:
    raw_data = [line.strip('\n').split(' ') for line in f]


""" PART ONE """

draw = [['A','X'], ['B','Y'], ['C','Z']]
win = [['A','Y'], ['B','Z'], ['C','X']]
lose = [['A','Z'], ['B','X'], ['C','Y']]

score = 0
for line in raw_data:
    if line in draw:
        score += 3
    elif line in win:
        score += 6
    elif line in lose:
        score += 0
    if line[1] == 'X':
        score += 1
    elif line[1] == 'Y':
        score += 2
    elif line[1] =='Z':
        score += 3

print(score)

""" PART TWO """

win = np.array([['A','B'],['B','C'],['C','A']])
lose = np.array([['A','C'],['B','A'],['C','B']])

score = 0
for line in raw_data:
    if line[1] == 'X':
        play = lose[np.where(lose[:,0] == line[0]),1]
    elif line[1] == 'Y':
        score += 3
        play = line[0]
    elif line[1] == 'Z':
        score += 6
        play = win[np.where(win[:,0] == line[0]),1]
    if play == 'A':
        score += 1
    elif play == 'B':
        score += 2
    elif play == 'C':
        score += 3

print(score)

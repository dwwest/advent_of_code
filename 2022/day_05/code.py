import numpy as np
import re

""" IMPORT DATA """ 

crates = {}
for i in range(1,10):
    crates[i] = []
moves = []
with open('input.txt','r') as f:
    for line in f:
        if '[' in line:
            for ind,i in enumerate(range(1,37,4)):
                if line[i] != ' ':
                    crates[ind+1].append(line[i])
        if 'move' in line:
            moves.append([int(i) for i in re.findall(r'\d+',line)])

""" PART ONE """

# for move in moves:
#     for num in range(move[0]):
#         to_move = crates[move[1]].pop(0)
#         crates[move[2]].insert(0, to_move)

# code = ''
# for i in range(1,10):
#     code += crates[i][0]
# print(code)

""" PART TWO """

for move in moves:
    to_move = crates[move[1]][0:move[0]]
    for num in range(move[0]):
        crates[move[1]].pop(0)
    to_move.reverse()
    for i in to_move:
        crates[move[2]].insert(0, i)

code = ''
for i in range(1,10):
    code += crates[i][0]
print(code)
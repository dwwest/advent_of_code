import numpy as np

""" IMPORT DATA """
moves = []
with open('input.txt','r') as f:
    for line in f:
        to_append = line.strip('\n').split(' ')
        moves.append([to_append[0],int(to_append[1])])

""" PART ONE """

h_pos = [0,0]
t_pos = [0,0]
t_pos_visited = []

for [move, num] in moves:
    for n in range(num):
        if move == 'U':
            h_pos[0] += 1
        elif move =='D':
            h_pos[0] -= 1
        elif move == 'R':
            h_pos[1] += 1
        elif move == 'L':
            h_pos[1] -= 1
        if abs(h_pos[0]-t_pos[0]) > 1. or abs(h_pos[1]-t_pos[1]) > 1.:
            if h_pos[0] == t_pos[0]:
                if h_pos[1] - t_pos[1] > 0.:
                    t_pos[1] += 1
                    t_pos_visited.append(tuple(t_pos))
                else:
                    t_pos[1] -= 1
                    t_pos_visited.append(tuple(t_pos))
            elif h_pos[1] == t_pos[1]:
                if h_pos[0] - t_pos[0] > 0.:
                    t_pos[0] += 1
                    t_pos_visited.append(tuple(t_pos))
                else:
                    t_pos[0] -= 1
                    t_pos_visited.append(tuple(t_pos))
            else:
                if h_pos[0] - t_pos[0] > 0.:
                    t_pos[0] += 1
                else:
                    t_pos[0] -= 1
                if h_pos[1] - t_pos[1] > 0.:
                    t_pos[1] += 1
                    t_pos_visited.append(tuple(t_pos))
                else:
                    t_pos[1] -= 1
                    t_pos_visited.append(tuple(t_pos))

print(len(list(set(t_pos_visited)))+1)

""" PART TWO """

all_pos = np.zeros((10,2))
t_pos_visited = []

def append_pos(all_pos, k):
    if k == 9:
        t_pos_visited.append(tuple(all_pos[9]))

for [move, num] in moves:
    for n in range(num):
        if move == 'U':
            all_pos[0,0] += 1
        elif move =='D':
            all_pos[0,0] -= 1
        elif move == 'R':
            all_pos[0,1] += 1
        elif move == 'L':
            all_pos[0,1] -= 1
        for k in range(1, len(all_pos)):
            if abs(all_pos[k-1, 0]-all_pos[k, 0]) > 1. or abs(all_pos[k-1, 1]-all_pos[k, 1]) > 1.:
                if all_pos[k-1, 0] == all_pos[k, 0]:
                    if all_pos[k-1, 1] - all_pos[k, 1] > 0.:
                        all_pos[k, 1] += 1
                        append_pos(all_pos, k)
                    else:
                        all_pos[k, 1] -= 1
                        append_pos(all_pos, k)
                elif all_pos[k-1, 1] == all_pos[k, 1]:
                    if all_pos[k-1, 0] - all_pos[k, 0] > 0.:
                        all_pos[k, 0] += 1
                        append_pos(all_pos, k)
                    else:
                        all_pos[k, 0] -= 1
                        append_pos(all_pos, k)
                else:
                    if all_pos[k-1,0] - all_pos[k,0] > 0.:
                        all_pos[k, 0] += 1
                    else:
                        all_pos[k, 0] -= 1
                    if all_pos[k-1, 1] - all_pos[k, 1] > 0.:
                        all_pos[k, 1] += 1
                        append_pos(all_pos, k)
                    else:
                        all_pos[k, 1] -= 1
                        append_pos(all_pos, k)

print(len(list(set(t_pos_visited)))+1)

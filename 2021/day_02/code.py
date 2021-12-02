import numpy as np


with open('input.txt') as f:
    l = [i.split(' ') for i in f.read().splitlines()]
for i in l:
    i[0] = str(i[0])
    i[1] = int(i[1])

# part 1
pos = [0, 0]
for instruct in l:
    if instruct[0] == 'up': 
        pos[0] -= instruct[1]
    elif instruct[0] == 'down':
        pos[0] += instruct[1]
    elif instruct[0] == 'forward':
        pos[1] += instruct[1]
print(pos[0]*pos[1])

# part 2
aim = 0
pos = [0, 0]
for instruct in l:
    if instruct[0] == 'up': 
        aim -= instruct[1]
    elif instruct[0] == 'down':
        aim += instruct[1]
    elif instruct[0] == 'forward':
        pos[1] += instruct[1]
        pos[0] += aim * instruct[1]
print(pos[0]*pos[1])   

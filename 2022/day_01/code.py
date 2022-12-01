import numpy as np


""" READ DATA """
raw_data = []
with open('input.txt', 'r') as f:
    for line in f:
        raw_data.append(line.strip('\n'))

""" PART ONE """
elves = []
current = 0
for line in raw_data:
    if line == '':
        elves.append(current)
        current = 0
    else:
        current += int(line)

print(np.max(elves))

""" PART TWO """

elves.sort(reverse=True)
print(np.sum(elves[0:3]))

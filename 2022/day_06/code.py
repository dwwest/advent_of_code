import numpy as np

""" IMPORT DATA """

raw_data = []
with open('input.txt', 'r') as f:
    for line in f:
        raw_data.append(line)

""" PART ONE """

for line in raw_data:
    for ind1,ind2 in zip(range(len(line)-4),range(4,len(line))):
        if len(set(line[ind1:ind2])) == 4:
            print(ind2)
            break

""" PART TWO """

for line in raw_data:
    for ind1,ind2 in zip(range(len(line)-14),range(14,len(line))):
        if len(set(line[ind1:ind2])) == 14:
            print(ind2)
            break
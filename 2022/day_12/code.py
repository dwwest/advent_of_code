import numpy as np

""" IMPORT DATA """

with open('test.txt', 'r') as f:
    map = f.read().splitlines()
map = np.array([[ord(i) - 96 for i in n] for n in map])
# get value of start = 0
start = np.where(map == -13)
map[start] = 0
# get value of end = 27
end = np.where(map == -27)
map[end] = 27

""" PART ONE """

paths = []
current_ind = np.concatenate(np.where(map == 0)).tolist()
paths.append([current_ind])
all_at_end = False
while not all_at_end:
    


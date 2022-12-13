
import numpy as np

""" IMPORT DATA """

with open('input.txt', 'r') as f:
    map = f.read().splitlines()
map = np.array([[ord(i) - 96 for i in n] for n in map])
# get value of start = 0
start = np.where(map == -13)
map[start] = 0
# get value of end = 27
end = np.where(map == -27)
map[end] = 27
map_max_i = np.shape(map)[0]
map_max_j = np.shape(map)[1]

""" PART ONE """

def breadth_first(queue):
    to_try = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    explored = []
    while len(queue) > 0:
        current = queue.pop(0)
        length = current[2]
        if map[current[0], current[1]] == 27:
            return(length)
        for t in [[n[0]+current[0],n[1]+current[1]] for n in to_try]:
            if 0 > t[0] or 0 > t[1] or t[0] >= map_max_i or t[1] >= map_max_j:
                continue
            if map[current[0], current[1]] + 1 < map[t[0], t[1]]:
                continue
            if t in explored:
                continue
            explored.append(t)
            queue.append([t[0], t[1], length+1])

queue = [np.concatenate(np.where(map == 0)).tolist()]
queue[0].append(0)
print(breadth_first(queue))

""" PART TWO """

starts = np.where(map == 1)
starts = [[starts[0][i],starts[1][i]] for i in range(np.shape(starts)[1])]
hike_lengths = []
for s in starts:
    queue = [list(s)]
    queue[0].append(0)
    hike_lengths.append(breadth_first(queue))
print(min(hike_lengths))

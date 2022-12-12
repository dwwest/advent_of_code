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

paths = [[np.concatenate(np.where(map == 0)).tolist()]]
to_try = [[1, 0,], [-1, 0], [0, 1], [0, -1]]
all_at_end = False
while not all_at_end:
    new_paths = []
    for path in paths:
        current_ind = path[-1]
        new_inds = [list(np.array(current_ind) + np.array(n)) for n in to_try]
        for t in new_inds:
            if all(i >= 0 for i in t) and t not in path and t[0] < map_max_i and t[1] < map_max_j:
                    if map[current_ind[0], current_ind[1]] + 1 == map[t[0], t[1]] or map[current_ind[0], current_ind[1]] == map[t[0], t[1]]:
                        if t not in path:
                            new_path = [p for p in path]
                            new_path.append(t)
                            new_paths.append(new_path)
    paths = new_paths
    if any(map[p[-1][0], p[-1][1]] == 27 for p in paths):
        all_at_end = True

print(min([len(p) for p in paths]) - 1)


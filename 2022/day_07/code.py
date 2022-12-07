import numpy as np

""" IMPORT DATA """
commands = []
with open('input.txt','r') as f:
    for line in f:
        commands.append(line.strip('\n'))

""" PART ONE """

tree = {}
dir_list = []
size_dir = {}
total_space = 0
for line in commands:
    if line[0] == '$':
        if 'cd' in line:
            if line == '$ cd ..':
                dir_list.pop()
            elif line == '$ cd /':
                dir_list = []
            else:
                dir_list.append(line[5:])
    else:
        current_directory = tree
        for d in dir_list:
            current_directory = current_directory[d]
        to_add = line.split(' ')
        if to_add[0] == 'dir':
            current_directory[to_add[1]] = {}
        else:
            current_directory[to_add[1]] = int(to_add[0])
            n = ''
            for d in dir_list:
                n += d + '/'
                if n not in size_dir:
                    size_dir[n] = 0
                size_dir[n] += int(to_add[0])
            total_space += int(to_add[0])

total_sum = 0
for k in size_dir.keys():
    if size_dir[k] <= 100000:
        total_sum += size_dir[k]
print(total_sum)

""" PART TWO """

space_needed = 30000000 - (70000000 - total_space)
possible_dirs = []
for k in size_dir.keys():
    if size_dir[k] >= space_needed:
        possible_dirs.append(size_dir[k])
possible_dirs.sort()
print(possible_dirs[0])
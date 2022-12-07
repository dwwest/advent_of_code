import numpy as np

commands = []
with open('input.txt','r') as f:
    for line in f:
        commands.append(line.strip('\n'))

tree = {}
dir_sizes = {}
dir_list = []
for line in commands[0:30]:
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
        if to_add[1] not in current_directory.keys():
            if 'dir' in line:
                current_directory[to_add[1]] = {}
                dir_sizes[to_add[1]] = 0
            else:
                current_directory[to_add[1]] = int(to_add[0])
                for d in dir_list:
                    dir_sizes[d] += int(to_add[0])

total_sum = 0
for d in dir_sizes.keys():
    if dir_sizes[d] <= 100000:
        total_sum += dir_sizes[d]
print(total_sum)
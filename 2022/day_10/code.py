import numpy as np

""" IMPORT DATA """

commands = []
with open('input.txt', 'r') as f:
    for line in f:
        commands.append(line.strip('\n'))

""" PART ONE """

# to_check = list(range(20, 260, 40))
# cycles = 1
# X = 1
# strengths = []

# def check():
#     if cycles in to_check:
#         strengths.append(cycles * X)

# for command in commands:
#     if command == 'noop':
#         check()
#         cycles += 1
#     elif command.split(' ')[0] == 'addx':
#         check()
#         cycles += 1
#         check()
#         cycles += 1
#         X += int(command.split(' ')[1])

# print(np.sum(strengths))

""" PART TWO """

crt = np.zeros((6, 40))

cycles = 1
X = [0,1,2]
crt_row = 0

def check_sprite():
    if cycles-1 in X:
        crt[crt_row, cycles-1] = 1

def check_row():
    global crt_row
    global cycles
    if cycles == 41:
        crt_row += 1
        cycles = 1

for command in commands:
    if command == 'noop':
        check_sprite()
        cycles += 1
        check_row()
    elif command.split(' ')[0] == 'addx':
        check_sprite()
        cycles += 1
        check_row()
        check_sprite()
        cycles += 1
        check_row()
        for i in range(len(X)):
            X[i] += int(command.split(' ')[1])

for n in crt:
    to_print = ''
    for i in n:
        if int(i) == 0:
            to_print += '.'
        else:
            to_print += '#'
    print(to_print)

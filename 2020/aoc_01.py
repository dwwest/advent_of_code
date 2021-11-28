import numpy

with open('day_01/input.txt') as f:
    l = [int(i) for i in f.read().splitlines()]

# part 1
for ind_one in range(len(l)-1):
    for ind_two in range(1, len(l)):
        if l[ind_one] + l[ind_two] == 2020:
            to_input = l[ind_one]*l[ind_two]
            break
print(to_input)

# part 2
for ind_one in range(len(l)-2):
    for ind_two in range(1, len(l)-1):
        for ind_three in range(2, len(l)):
            if l[ind_one] + l[ind_two] + l[ind_three] == 2020:
                to_input = l[ind_one]*l[ind_two]*l[ind_three]
                break
print(to_input)




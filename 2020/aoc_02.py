import numpy

with open('day_02/input.txt') as f:
    l = [i.split() for i in f.read().splitlines()]

# part 1
num_good_passwords = 0
for i in l:
    count = i[2].count(i[1][0])
    start_end = [int(n) for n in i[0].split('-')]
    r = [i for i in range(start_end[0], start_end[1]+1)]
    if count in r:
        num_good_passwords += 1 
print(num_good_passwords)

# part 2
num_good_passwords = 0
for i in l:
    letter = i[1][0]    
    pos = [int(n)-1 for n in i[0].split('-')]
    num_letter_at_pos = 0
    for p in pos:
        if letter == i[2][p]:
            num_letter_at_pos += 1
    if num_letter_at_pos == 1:
        num_good_passwords += 1
print(num_good_passwords)


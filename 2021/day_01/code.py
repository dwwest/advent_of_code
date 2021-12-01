import numpy as np

with open('input.txt') as f:
    l = [int(i) for i in f.read().splitlines()]

# part 1
num_increases = 0
last = l[0]
for i in l[1:]:
    if last < i:
        num_increases += 1
    last = i
print(num_increases)

# part 2
num_increases = 0
last = l[0] + l[1] + l[2]
window = 3
for i in range(1, len(l) - window + 1):
    s = sum([l[i + n] for n in range(window)])
    if last < s:
        num_increases += 1
    last = s
print(num_increases)

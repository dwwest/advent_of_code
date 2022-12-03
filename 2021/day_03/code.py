import numpy as np

with open('input.txt') as f:
    l = [[int(n) for n in i] for i in f.read().splitlines()]
l = np.array(l)

gamma = []
epsilon = []
for ind, i in enumerate(l[0]):
    gamma.append(str(np.bincount(l[:,ind]).argmax()))
    epsilon.append(str(np.bincount(l[:,ind]).argmin()))
print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))




import numpy as np

""" LOAD DATA """
assigns = []
with open('input.txt','r') as f:
    for line in f:
        assigns.append([[int(n) for n in i.split('-')] for i in line.strip('\n').split(',')])

""" PARTS ONE AND TWO """

subsets = 0
overlaps = 0
for a in assigns:
    set_one = set([i for i in range(a[0][0],a[0][1]+1)])
    set_two = set([i for i in range(a[1][0],a[1][1]+1)])
    """ PART ONE"""
    if set_one.issubset(set_two) or set_two.issubset(set_one):
        subsets += 1
    """ PART TWO """
    if len(list(set_one.intersection(set_two))) != 0:
        overlaps += 1

print(subsets)
print(overlaps)

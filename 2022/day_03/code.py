import numpy as np
import string

""" IMPORT DATA """

bags = []
with open('input.txt', 'r') as f:
    for line in f:
        bags.append([set(line.strip('\n')[:len(line)/2]),set(line.strip('\n')[len(line)/2:])])

""" PART ONE """
priorities = {}
for a, score in zip(list(string.ascii_lowercase),range(1,27)):
    priorities[a] = score
for A, score in zip(list(string.ascii_uppercase),range(27,53)):
    priorities[A] = score

total = 0
for bag in bags:
    total += priorities[list(bag[0].intersection(bag[1]))[0]]

print(total)

""" PART TWO """
grouped_compartments = [i[0] | i[1] for i in bags]
elf_groups = [grouped_compartments[i:i+3] for i in range(0,len(grouped_compartments),3)]
total = 0
for group in elf_groups:
    total += priorities[list(group[0] & group[1] & group[2])[0]]
print(total)

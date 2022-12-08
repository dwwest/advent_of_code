import numpy as np
import sys

""" IMPORT DATA """

tree_grid = []
with open('input.txt', 'r') as f:
    for line in f:
        tree_grid.append([int(i) for i in line.strip('\n')])

tree_grid = np.array(tree_grid)
is_visible = np.zeros(np.shape(tree_grid))

""" PART ONE """

for row_ind, row in enumerate(tree_grid):
    for col_ind, tree in enumerate(row):
        if row_ind == 0 or row_ind == np.shape(tree_grid)[0]-1 or col_ind == 0 or col_ind == np.shape(tree_grid)[1]-1:
            is_visible[row_ind, col_ind] = 1
        elif tree > np.max(tree_grid[row_ind,:col_ind]) or tree > np.max(tree_grid[row_ind,col_ind+1:]):
            is_visible[row_ind,col_ind] = 1
        elif tree > np.max(tree_grid[:row_ind:,col_ind]) or tree > np.max(tree_grid[row_ind+1:,col_ind]):
            is_visible[row_ind,col_ind] = 1

print(np.sum(is_visible))

""" PART TWO """

def check_tree(tree, adjs):
    to_return = 0
    if len(adjs) == 0:
        return(0)
    else:
        for adj in adjs:
            if adj < tree:
                to_return += 1
            elif adj >= tree:
                to_return +=1
                return(to_return)
    return(to_return)
        
highest_scenic_score = 0
for row_ind, row in enumerate(tree_grid):
    for col_ind, tree in enumerate(row):
        current_scenic_score = 1
        for adjs in [np.flip(tree_grid[row_ind,:col_ind]), tree_grid[row_ind,col_ind+1:], \
            np.flip(tree_grid[:row_ind:,col_ind]), tree_grid[row_ind+1:,col_ind]]:
            current_scenic_score *= check_tree(tree, adjs)
        if current_scenic_score > highest_scenic_score:
            highest_scenic_score = current_scenic_score
print(highest_scenic_score)

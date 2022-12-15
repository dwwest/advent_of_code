import numpy as np

""" IMPORT DATA """

packets = []
with open('input.txt', 'r') as f:
    packets = [i.split('\n') for i in f.read().split('\n\n')]

""" PART ONE """

def check_order(i, j):
    if type(i) == int:
        if type(j) != int:
            return(check_order([i], j))
    if type(j) == int:
        if type(i) != int:
            return(check_order(i, [j]))
        if type(j) == int:
            if i < j:
                return(True)
            if i > j:
                return(False)
    if type(i) == list and type(j) == list:
        for c in range(max(len(i), len(j))):
            if c > len(j)-1:
                return(False)
            if c > len(i)-1:
                return(True)
            if check_order(i[c], j[c]) != None:
                return(check_order(i[c], j[c]))

# inds_right = []
# for i, p in enumerate(packets):
#     if check_order(eval('list(' + p[0] + ')'), eval('list(' + p[1] + ')')):
#         inds_right.append(i+1)

# print(sum(inds_right))

""" PART TWO """

def reorder_inds(is_larger, p_ind):
    insert_ind = 0
    for i in is_larger:
        if i == True:
            break
        else:
            insert_ind += 1
    return(insert_ind)

all_packets = []
for p in packets:
    all_packets.append(p[0])
    all_packets.append(p[1])
all_packets.append('[[2]]')
all_packets.append('[[6]]')

ordered_inds = [] # ordered inds from in original list
for p_ind, p in enumerate(all_packets):
    if len(ordered_inds) == 0:
        ordered_inds.append(0)
    else:
        is_larger = []
        for c in ordered_inds:
            is_larger.append(check_order(eval('list(' + p + ')'), eval('list(' + all_packets[c] + ')')))
        ordered_inds.insert(reorder_inds(is_larger, p_ind), p_ind)

ordered_packets = [all_packets[p] for p in ordered_inds]
print((ordered_packets.index('[[2]]')+1) * (ordered_packets.index('[[6]]')+1))
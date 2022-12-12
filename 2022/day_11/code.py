import numpy as np
import re

""" IMPORT DATA """

monkeys = {}

monkey_text = re.compile(r'''Monkey (\d):
\s*Starting items:\s*((?:\d+, )*\d+)
\s*Operation: new = old (.*)
\s*Test: divisible by (\d+)
\s*If true: throw to monkey (\d+)
\s*If false: throw to monkey (\d+)''', re.MULTILINE)

with open('input.txt', 'r') as f:
    raw_dat = f.read()

monkey_dat = re.findall(monkey_text,raw_dat)
for i in monkey_dat:
    monkeys[int(i[0])] = {'items':[int(n) for n in i[1].split(', ')],'op':i[2],'test':int(i[3]),'true':int(i[4]),'false':int(i[5])}

""" PART ONE """

def do_op(op, item):
    op_parts = op.split(' ')
    if op_parts[1] == 'old':
        to_op = item
    else:
        to_op = int(op_parts[1])
    if op_parts[0] == '+':
        return(item + to_op)
    elif op_parts[0] == '*':
        return(item * to_op)
        
inspections = np.zeros(len(monkeys.keys()))
for round in range(20):
    for monkey_num in range(len(monkeys.keys())):
        to_throw = []
        for el, item in enumerate(monkeys[monkey_num]['items']):
            worry_level = do_op(monkeys[monkey_num]['op'], item)/3
            if worry_level % monkeys[monkey_num]['test'] == 0:
                to_throw.append([worry_level, monkeys[monkey_num]['true']])
            else:
                to_throw.append([worry_level, monkeys[monkey_num]['false']])
            inspections[monkey_num] += 1
        monkeys[monkey_num]['items'] = []
        for item in to_throw:
            monkeys[item[1]]['items'].append(item[0])

print(np.prod(np.sort(inspections)[-2:]))

""" PART TWO """

with open('input.txt', 'r') as f:
    raw_dat = f.read()

monkey_dat = re.findall(monkey_text,raw_dat)
for i in monkey_dat:
    monkeys[int(i[0])] = {'items':[int(n) for n in i[1].split(', ')],'op':i[2],'test':int(i[3]),'true':int(i[4]),'false':int(i[5])}

modulus = np.prod(np.array([monkeys[num]['test'] for num in monkeys.keys()]))
inspections = np.zeros(len(monkeys.keys()))
for round in range(10000):
    for monkey_num in range(len(monkeys.keys())):
        to_throw = []
        for el, item in enumerate(monkeys[monkey_num]['items']):
            worry_level = do_op(monkeys[monkey_num]['op'], item)
            worry_level = worry_level % modulus
            if worry_level % monkeys[monkey_num]['test'] == 0:
                to_throw.append([worry_level, monkeys[monkey_num]['true']])
            else:
                to_throw.append([worry_level, monkeys[monkey_num]['false']])
            inspections[monkey_num] += 1
        monkeys[monkey_num]['items'] = []
        for item in to_throw:
            monkeys[item[1]]['items'].append(item[0])

print(np.prod(np.sort(inspections)[-2:]))
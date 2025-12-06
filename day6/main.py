import re
from functools import reduce

def read_input(filename):
    with open(filename, 'r') as f:
        return [x.replace('\n', '') for x in f.readlines() if x.strip()]

def parse1(data):
    data = [[y for y in x.strip().split(" ") if y] for x in data]
    probs = [[] for x in range(len(data[0]))]
    for row in data[:-1]:
        for i in range(len(row)):
            probs[i].append(row[i])
    return probs, data[-1]

def parse2(data):
    op_inds = [i for i in range(len(data[-1])) if data[-1][i] in '*+']
    ops = [data[-1][i] for i in op_inds]
    op_inds.append(len(data[0])+1)
    probs = []
    for s, e in zip(op_inds, op_inds[1:]):
        prob = [0 for i in range(s, e-1)]
        for row in data[:-1]:
            for i in range(s, e-1):
                try:
                    val = int(row[i])
                    prob[i-s] = prob[i-s]*10 + val
                except:
                    pass
        probs.append(prob)
    return probs, ops

def operate(nums, ops):
    return sum([reduce(lambda x, y: int(x)*int(y), nums[i]) \
                if ops[i] == '*' else \
                reduce(lambda x, y: int(x)+int(y), nums[i]) \
                for i in range(len(ops))])

def part1(data):
    nums, ops = parse1(data)
    return operate(nums, ops)

def part2(data):
    nums, ops = parse2(data)
    return operate(nums, ops)

if __name__ == "__main__":
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))

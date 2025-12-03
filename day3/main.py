def read_input(s):
    with open(s, 'r') as f:
        data = [x.strip() for x in f.readlines() if x]
    return data

def find_max_parts(s, size=2):
    maxes = [0 for i in range(size)]
    for i, v in enumerate(s):
        vi = int(v)
        placed = False
        for j in range(size):
            if placed:
                continue
            if vi > maxes[j] and i < len(s)-size+j+1:
                maxes[j] = vi
                for k in range(j+1, size):
                    maxes[k] = 0
                placed = True
    return maxes

def part1(data):
    tot = 0
    for bs in data:
        vals = find_max_parts(bs)
        tot += sum([10**(k) * v for k, v in enumerate(reversed(vals))])
    return tot

def part2(data):
    tot = 0
    for bs in data:
        vals = find_max_parts(bs, size=12)
        tot += sum([10**(k) * v for k, v in enumerate(reversed(vals))])
    return tot

if __name__ == "__main__":
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))


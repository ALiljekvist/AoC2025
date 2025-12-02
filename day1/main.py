def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.readlines()]
    return data

# TODO: Make efficient by subtracting the remaining
# value to make a full turn until the value reaches 0
# instead adding 1 by 1 and 
def rot(curr, value, mod=100):
    tot = 0
    mult = 1 if value[0] == 'R' else -1
    to_add = int(value[1:])
    for _ in range(to_add):
        curr += mult
        curr = (curr % mod + mod) % mod
        if curr == 0:
            tot += 1
    return curr, tot

def part1(data):
    count = 0
    curr = 50
    for val in data:
        curr, _ = rot(curr, val)
        if curr == 0:
            count += 1
    return count

def part2(data):
    tot = 0
    curr = 50
    for val in data:
        curr, sub = rot(curr, val)
        tot += sub
    return tot

if __name__ == "__main__":
    data = read_input("input.txt")
    print(part1(data))
    print(part2(data))

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
    return lines

def to_rolls(data):
    rolls = {}
    dim1, dim2 = len(data), len(data[0])
    for i in range(dim1):
        for j in range(dim2):
            if data[i][j] == '@':
                rolls[(i, j)] = 1
    return rolls, (dim1, dim2)

def check_reachable(rolls, i, j):
    return sum([sum([rolls.get((k,l), 0) for l in range(j-1, j+2)])for k in range(i-1, i+2)])-1 < 4


def part1(data):
    rolls, (d1, d2) = to_rolls(data)
    return sum([sum([check_reachable(rolls, i, j) if (i,j) in rolls else 0 for j in range(d2)]) for i in range(d1)])

def part2(data):
    rolls, (d1, d2) = to_rolls(data)
    done = False
    removed = 0
    while not done:
        to_remove = []
        for i in range(d1):
            for j in range(d2):
                if (i,j) in rolls and check_reachable(rolls, i, j):
                    to_remove.append((i,j))
        if not to_remove:
            done = True
        removed += len(to_remove)
        for roll in to_remove:
            rolls.pop(roll)
    return removed

if __name__ == "__main__":
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))


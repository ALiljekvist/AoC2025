def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    parts = [x.strip().split('\n') for x in data.split('\n\n') if x.strip()]
    return [[int(y) for y in x.split('-')] for x in parts[0]], [int(x) for x in parts[1]]

def part1(data):
    return sum([any([x[0] <= id <= x[1] for x in data[0]]) for id in data[1]])

def part2(data):
    consolidated_ranges = []
    sorted_ranges = sorted(data[0], key=lambda x: x[0])
    for s,e in sorted_ranges:
        for _, ei in consolidated_ranges:
            if s <= ei:
                s = ei+1
        if e < s:
            # This is now an invalid range
            continue
        consolidated_ranges.append([s, e])
    return sum([e-s+1 for s,e in consolidated_ranges])

if __name__ == "__main__":
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))

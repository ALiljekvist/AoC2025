def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.read().split(',')]
    return [[int(y) for y in x.split('-')] for x in data]

def check_invalid(id) -> int:
    str_id = str(id)
    return id if str_id[len(str_id)//2:] == str_id[:len(str_id)//2] else 0

def part1(data):
    return sum(sum([check_invalid(id) for id in range(x[0], x[1]+1)]) for x in data)

# TODO: Return next number that could possibly be invalid
def check_invalid2(id) -> int:
    str_id = str(id)
    for win in range(1, len(str_id) // 2 + 1):
        splits = [str_id[i:i+win] for i in range(0, len(str_id)-win)]
        if all([x == splits[0] for x in splits]):
            return id
    return 0

def part2(data):
    return sum(sum([check_invalid2(id) for id in range(x[0], x[1]+1)]) for x in data)

if __name__ == "__main__":
    data = read_input("input.txt")
    print(part1(data))
    print(part2(data))

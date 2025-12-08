def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.readlines() if x.strip()]
    return [[int(y) for y in x.split(',')] for x in data]

def dist_sq(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

def find(circuits, i):
    for j in range(len(circuits)):
        if i in circuits[j]:
            return j
    return -1

def connect(data, lim=1000):
    dists = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            dists.append((dist_sq(data[i], data[j]), i, j))
    dists.sort(key=lambda x: x[0])
    circuits = [set([i]) for i in range(len(data))]
    part1 = 0
    for num, (_, i, j) in enumerate(dists):
        if num == lim:
            longest = sorted([len(x) for x in circuits], reverse=True)
            part1 = longest[0]*longest[1]*longest[2]
        c_i = find(circuits, i)
        c_j = find(circuits, j)
        if c_i == c_j:
            continue
        circuits[c_i].update(circuits.pop(c_j))
        if len(circuits) == 1:
            return part1, data[i][0]*data[j][0]
    return 

if __name__ == "__main__":
    data = read_input('input.txt')
    p1, p2 = connect(data)
    print(p1, p2)

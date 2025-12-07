def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.readlines() if x.strip()]
    return data

def add_new_beams(beams, new_beams, old_pos, new_pos):
    new_beams[new_pos] = new_beams.get(new_pos, 0) + beams[old_pos]

def split_beams(beams, splitters):
    new_beams = {}
    num_splits = 0
    for beam in beams:
        if beam in splitters.keys():
            add_new_beams(beams, new_beams, beam, (beam[0]+1, beam[1]-1))
            add_new_beams(beams, new_beams, beam, (beam[0]+1, beam[1]+1))
            num_splits += 1
            continue
        add_new_beams(beams, new_beams, beam, (beam[0]+1, beam[1]))
    return new_beams, num_splits

def part1_2(data):
    splitters = {}
    for i in range(len(data)):
        splitters.update(dict([((i,j), 1) for j in range(len(data[i])) if data[i][j] == '^']))
    beams = {(0, data[0].find('S')): 1}
    splits = 0
    for _ in range(len(data)):
        beams, new_splits = split_beams(beams, splitters)
        splits += new_splits
    return splits, sum([num for _, num in beams.items()])

if __name__ == "__main__":
    data = read_input('input.txt')
    p1, p2 = part1_2(data)
    print(p1)
    print(p2)

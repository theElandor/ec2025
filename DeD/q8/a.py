import sys
filename = sys.argv[1]
with open(filename) as f:
    moves = [int(x) for x in f.read().split(",")]
    nails = 32
    dist = nails // 2
    counter = 0
    current = moves[0]
    for move in moves[1:]:
        if abs(current -move) == dist:
            counter += 1
        current = move
    print(counter)
        

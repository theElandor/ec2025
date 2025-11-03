import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().split("\n\n")
    names = data[0].strip().split(",")
    moves = data[1].strip().split(",")
    index = 0
    for d,m in moves:
        m = int(m)
        if d == "R":
            index = min(len(names)-1, index+m)
        if d == "L":
            index = max(0, index-m)
    print(names[index])

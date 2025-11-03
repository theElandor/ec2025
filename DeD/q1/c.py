import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().split("\n\n")
    names = data[0].strip().split(",")
    moves = data[1].strip().split(",")
    index = 0
    for s in moves:
        d = s[0]
        m = int(s[1:])
        index = 0
        if d == "R":
            index = (index+m)%len(names)
        if d == "L":
            index = (index-m)%len(names)
        print(index)
        names[0],names[index] = names[index], names[0]
        print(names)
    print(names[0])

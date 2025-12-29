import sys
from collections import deque
filename = sys.argv[1]
with open(filename) as f:
    ranges = [tuple(map(int, x.split("-"))) for x in f.read().splitlines()]
    r = []
    l = []
    for i,(s,e) in enumerate(ranges):
        for x in range(s,e+1):
            if i % 2 == 0:
                r.append(x)
            else:
                l.append(x)
    seq = [1] + r + l[::-1]
    print(seq[20252025 % len(seq)])
            


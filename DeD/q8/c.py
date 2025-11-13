import sys
from itertools import combinations
filename = sys.argv[1]
nails = 256

def check_pair(l1, lines):
    x1,x2 = l1
    knots = 0
    for y1, y2 in lines:
         # check previous lines
         if sorted((x1,x2)) == sorted((y1,y2)):
             knots += 1
             continue
         if x1 == y1 or x1 == y2 or x2 == y1 or x2 == y2:
             continue
         prev_found = None
         for index in range(1,nails+1):
             # x1,x2, y1, y2 are for sure different.
             if index in [x1,x2]:
                 if prev_found == "x":
                     break
                 prev_found = "x"
             elif index in [y1,y2]:
                 if prev_found == "y": 
                     break
                 prev_found = "y"
         else:
             knots += 1
    return knots

with open(filename) as f:
    moves = [int(x) for x in f.read().split(",")]
    lines = [(x1,x2) for x1,x2 in zip(moves[:-1], moves[1:])]
    combs = list(combinations([x+1 for x in range(nails)],2))
    start = 20000
    m = -float("inf")
    n = len(combs)
    for i,(c1,c2) in enumerate(combs[start:]):
        if i % 100 == 0:
            print("{}/{}".format(start+i,n))
            print(m)
        m = max(m, check_pair((c1,c2), lines))
    print(m)

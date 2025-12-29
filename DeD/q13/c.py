'''
Cool problem with ranges, easy to solve 
but also easy to write stupid bugs.
'''


import sys
from collections import deque
filename = sys.argv[1]
with open(filename) as f:
    ranges = [tuple(map(int, x.split("-"))) for x in f.read().splitlines()]
    # this code worked also for part 3, even if it was a little slow
    #r = []
    #l = []
    #for i,(s,e) in enumerate(ranges):
    #    for x in range(s,e+1):
    #        if i % 2 == 0:
    #            r.append(x)
    #        else:
    #            l.append(x)
    #seq = [1] + r + l[::-1]
    #print(seq[202520252025 % len(seq)]) 

    # faster version looks like this:
    r = [x for i,x in enumerate(ranges) if i % 2 == 0] 
    l = [x for i,x in enumerate(ranges) if i % 2 != 0]
    seq = [(1,1)] + r + l[::-1]
    pos = 202520252025 % sum((e-s)+1 for s,e in seq)
    c = 0
    for s,e in seq:
        ilen = e - s +1
        if c + ilen > pos:
            if (s,e) in r: print(s+pos-c)
            else: print(e-pos+c)
            break
        else: c += ilen

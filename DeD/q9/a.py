import sys
from collections import Counter
filename = sys.argv[1]
with open(filename) as f:
    scales = [x.split(":")[1] for x in f.read().splitlines()]
    wrongs = set()
    ans = 0
    for x,y,z in zip(*scales):
        print(x,y,z)
        t = Counter([x,y,z])
        if len(t) == 1:
            continue
        k,v = t.most_common()[0]
        if v == 1: continue
        # find != k 
        if x != k:
            wrongs.add(0)
        elif y != k:
            wrongs.add(1)
        elif z != k:
            wrongs.add(2)
        if len(wrongs) == 2:
            break
    # index of child
    child = (set([0,1,2]) - wrongs).pop()
    child_scale = scales[child]
    parents = [x for i,x in enumerate(scales) if i != child]
    vals = []
    ans = 1
    for i, scale in enumerate(parents, start=1):
        print(i, scale)
        result =sum([x == y for x,y in zip(child_scale, scale)]) 
        print(result)
        ans *= result 
    print(ans)
        

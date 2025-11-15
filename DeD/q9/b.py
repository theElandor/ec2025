import sys
from collections import Counter
from itertools import combinations
from collections import defaultdict
filename = sys.argv[1]
with open(filename) as f:
    all_scales = [x.split(":")[1] for x in f.read().splitlines()]
    triplets = combinations(range(len(all_scales)), 3)
    res = defaultdict(int)
    for triplet in triplets:
        scales = [x for i, x in enumerate(all_scales) if i in triplet]
        wrongs = set()
        for x,y,z in zip(*scales):
            t = Counter([x,y,z])
            if len(t) == 1: # x = y = z 
                continue
            k,v = t.most_common()[0]
            if v == 1: continue # x != y != z
            # find != k 
            if x != k:
                wrongs.add(0)
            elif y != k:
                wrongs.add(1)
            elif z != k:
                wrongs.add(2)
        # index of child
        if len(wrongs) in [0,1,3]: continue
        child = (set([0,1,2]) - wrongs).pop()
        child_scale = scales[child]
        parents = [x for i,x in enumerate(scales) if i != child]
        vals = []
        temp = 1
        print(triplet)
        for i, scale in enumerate(parents, start=1):
            result =sum([x == y for x,y in zip(child_scale, scale)])
            temp *= result
        res[triplet[child]] = temp
    print(sum(res.values())) 

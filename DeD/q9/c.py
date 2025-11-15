import sys
from collections import Counter
from itertools import combinations
from collections import defaultdict
filename = sys.argv[1]
visited = set()
def dfs(n, G):
    visited.add(n)
    if n not in G:
        return n+1, 1
    s, c = 0,1
    for v in G[n]:
        if v not in visited:
            s_, c_ = dfs(v, G)
            s += s_
            c += c_ 
    return s + (n+1), c
    
with open(filename) as f:
    all_scales = [x.split(":")[1] for x in f.read().splitlines()]
    triplets = combinations(range(len(all_scales)), 3)
    res = {}
    triplets = list(triplets)
    L = len(triplets)
    for index, triplet in enumerate(triplets):
        if index % 1000 == 0:
            print(f"{index}/{L}") 
        scales = [x for i, x in enumerate(all_scales) if i in triplet]
        wrongs = set()
        for x,y,z in zip(*scales):
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
        # index of child
        if len(wrongs) in [0,1,3]: continue
        child = (set([0,1,2]) - wrongs).pop()
        child_scale = scales[child]
        parents = [x for i,x in enumerate(scales) if i != child]
        parents_i = [i for i,x in enumerate(scales) if i != child]
        vals = []
        temp = 1
        for i, scale in enumerate(parents, start=1):
            result =sum([x == y for x,y in zip(child_scale, scale)])
            temp *= result 
        a = triplet[parents_i[0]]
        b = triplet[parents_i[1]]
        c = triplet[child]
        # skip all triplets with a and b
        if c not in res:
            res[c] = [temp, a,b]
        else:
            old = res[c][0]
            if old < temp:
                res[c] = [temp, a, b]
    all_nodes = set()
    print(res)
    for k,v in res.items():
        all_nodes.add(k)
        for n in v[1:]:
            all_nodes.add(n)
    T = defaultdict(set)
    for k, v in res.items():
        #k -> v[1], v[2]
        T[v[1]].add(v[2])
        T[v[2]].add(v[1])
        T[v[1]].add(k)
        T[k].add(v[1])
    poss = []
    print("Start visit")
    print(T)
    for n in all_nodes:
       poss.append(dfs(n, T))
    print(max(poss, key=lambda x:x[1]))
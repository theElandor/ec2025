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
    s, c = n+1,1
    for v in G[n]:
        if v not in visited:
            s_, c_ = dfs(v, G)
            s += s_
            c += c_ 
    return s, c


with open(filename) as f:
    all_scales = [x.split(":")[1] for x in f.read().splitlines()]
    pairs = combinations(range(len(all_scales)), 2)
    res = {}
    skip = set()
    for p1, p2 in pairs: 
        if(p1,p2) in skip:
            continue
        for kid in range(len(all_scales)):
            if kid == p1 or kid == p2:
                continue
            scales = [all_scales[p1], all_scales[p2], all_scales[kid]]
            common = 0
            valid_kid = True
            for x,y,z in zip(*scales):
                if x == y and x != z:
                    valid_kid = False
                    break
                elif x == y == z:
                    common += 1
            else:
                if common == 0:
                    continue # with next kid
            if not valid_kid: continue
            # valid p1,p2 kid!
            # index of child
            p1_scale, p2_scale, child_scale = scales
            vals = []
            temp = 1
            for scale in enumerate([p1_scale,p2_scale]):
                result =sum([x == y for x,y in zip(child_scale, scale)])
                temp *= result 
            # skip all triplets with a and b
            # This assumption is wrong, kid and parent can
            # make another kid.
            for j in range(len(all_scales)):
                skip.add((p1,kid))
                skip.add((p2,kid))
                skip.add((kid,p1))
                skip.add((kid,p2))
            if kid not in res:
                res[kid] = [temp, p1,p2]
            else:
                old = res[kid][0]
                if old < temp:
                    res[kid] = [temp, p1, p2]
    all_nodes = set(range(len(all_scales)))
    T = defaultdict(set)
    for k, v in res.items():
        #k -> v[1], v[2]
        T[v[1]].add(v[2])
        T[v[2]].add(v[1])
        T[v[2]].add(k)
        T[k].add(v[2])
        T[v[1]].add(k)
        T[k].add(v[1])
    poss = []
    print("Start visit")
    print(T)
    for n in all_nodes:
       poss.append(dfs(n, T))
    print(max(poss, key=lambda x:x[1]))
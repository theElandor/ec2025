import sys

with open(sys.argv[1]) as f:
    ducks = [int(x) for x in f.read().splitlines()]
    all_ducks = sum(ducks)
    cols = len(ducks)
    per_col = all_ducks / cols
    checks = []
    while True:
        changes = 0
        checks.append(sum([ducks[i]*(i+1) for i in range(len(ducks))]))
        for c in range(cols-1):
            if ducks[c+1] < ducks[c]:
                ducks[c] -= 1
                ducks[c+1] += 1
                changes += 1
        if not changes:
            break
    print(ducks)
    first = True
    while True:
        changes = 0 
        if not first:
            checks.append(sum([ducks[i]*(i+1) for i in range(len(ducks))]))
        first = False
        for c in range(cols-1):
            if ducks[c+1] > ducks[c]:
                ducks[c+1] -= 1
                ducks[c] += 1
                changes += 1               
        if not changes:
            break
    print(len(checks)-1)


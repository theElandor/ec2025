import sys
filename = sys.argv[1]
total = set()
def visit(G, current):
    if 7 <= len(current) <= 11:
        total.add(current)
    if len(current) > 11:
        return
    if current[-1] not in G: return
    for v in G[current[-1]]:
        visit(G, current+v)

def check_prefix(name, rules):
    for x,y in zip(name[:-1], name[1:]):
        sill_valid = False
        for rule in rules:
            left, right = rule.split(" > ")
            right = right.split(",")
            if x == left and y in right:
                sill_valid = True
                break
        if not sill_valid:
            return False
    return True

with open(filename) as f:
    data = f.read().split("\n\n")
    prefixes = data[0].split(",")
    lines = data[1].splitlines()
    G = {}
    for line in lines:
        left, right = line.split(" > ") 
        right = right.split(",")
        if left not in G:
            G[left] = right
        else:
            G[left] += right

    for prefix in prefixes:
        if check_prefix(prefix, lines):
            visit(G, prefix)
    print(len(total))
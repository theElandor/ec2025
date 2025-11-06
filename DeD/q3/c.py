import sys
filename = sys.argv[1]
crates = [int(x) for x in open(filename).read().split(",")]
s = sorted(crates)

counter = 0
while s:
    taken = sorted(set(s))
    for x in taken:
        s.remove(x)
    counter += 1
print(counter)
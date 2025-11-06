import sys
filename = sys.argv[1]
crates = [int(x) for x in open(filename).read().split(",")]
s = sorted(crates)
counter = {s.count(c) for c in s}
print(max(counter))
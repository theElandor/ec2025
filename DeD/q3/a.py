import sys
filename = sys.argv[1]
crates = [int(x) for x in open(filename).read().split(",")]
s = sorted(crates)
prev = s[0]
res = prev
i = 1
while i < len(s):
    current = s[i]
    if current != prev:
        res += current
    i += 1
    prev = current
print(res)
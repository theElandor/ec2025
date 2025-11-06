import sys
filename = sys.argv[1]
crates = [int(x) for x in open(filename).read().split(",")]
s = sorted(crates)
print(s)
prev = s[0]
res = prev
i = 1
taken = 1
while i < len(s):
    if taken == 20:
        break
    current = s[i]
    if current != prev:
        res += current
        taken += 1
    i += 1
    prev = current
print(res)
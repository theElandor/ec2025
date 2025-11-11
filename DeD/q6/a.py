import sys
filename = sys.argv[1]
with open(filename) as f:
    letters = f.read().strip()
    prefix = []
    current = 0
    for l in letters:
        if l == 'A':
            current += 1
        prefix.append(current)
    ans = 0
    for i,x in enumerate(letters):
        if x == 'a':
            ans += prefix[i]
    print(ans)

import sys
filename = sys.argv[1]
def cast(t, data):
    ans = ""
    for i,x in enumerate(data):
        if t != x:
            ans = data[i+1:]
            return ans
    return ans

with open(filename) as f:
    data = f.read().splitlines()[0]
    flufs = ["R", "G","B"]
    total = 0
    while data:
        current = flufs[total%3]
        data = cast(current, data)
        total += 1
    print(total)
import sys
def eni(n,exp,mod):
    reminders = []
    score = 1
    for _ in range(exp):
        score = (score*n)%mod
        reminders.append(score)
    return int("".join([str(x) for x in reminders[::-1]]))

filename = sys.argv[1]
with open(filename) as f:
    lines = f.read().splitlines()
    vars = [v.split() for v in lines] 
    res = []
    for varset in vars:
        d = {}
        for var in varset:
            name, value = var.split("=")
            value = int(value)
            d[name] = value
        print(d)
        res.append(sum([eni(d['A'], d['X'], d['M']),eni(d['B'], d['Y'], d['M']),eni(d['C'], d['Z'], d['M'])])) 
        print(res[-1])
    print(max(res))

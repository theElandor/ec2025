import sys
def eni(n,exp,mod):
    reminders = []
    score = n%mod
    seen = {}
    i = 0
    while score not in seen:
        reminders.append(score)
        seen[score] = i
        i+=1
        score = (score*n)%mod
    period = reminders[seen[score]:i] 
    left = exp - i
    times = (left // len(period))
    i += (times*len(period))
    total = sum(reminders)
    total += sum(period)*times
    while i < exp:
        total += score
        i+=1
        score = (score*n)%mod 
    return total

filename = sys.argv[1]
with open(filename) as f:
    lines = f.read().splitlines()
    vars = [v.split() for v in lines] 
    print(eni(3,8,16))
    res = []
    for varset in vars:
        d = {}
        for var in varset:
            name, value = var.split("=")
            value = int(value)
            d[name] = value
        res.append(sum([eni(d['A'], d['X'], d['M']),eni(d['B'], d['Y'], d['M']),eni(d['C'], d['Z'], d['M'])])) 
    print(max(res))

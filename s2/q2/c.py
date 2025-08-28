import sys
filename = sys.argv[1]
def cast(t, data):
    if (len(data)%2) != 0:
        data = data[1:]
    else:
        if t == data[0]:
            data = data[:len(data)//2] + data[len(data)//2+1:]
        data = data[1:]
    return data

def fun(times, sequence):
    data = sequence*times
    total = 0
    while data:
        current = flufs[total%3]
        data = cast(current, data)
        total += 1   
    return total
with open(filename) as f:
    sequence = f.read().splitlines()[0]
    flufs = ["R", "G","B"]
    RES = {}
    print(fun(10, sequence)) 
    print(fun(6,sequence) + fun(4,sequence))
    
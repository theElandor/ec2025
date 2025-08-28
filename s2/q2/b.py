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
with open(filename) as f:
    sequence = f.read().splitlines()[0]
    flufs = ["R", "G","B"]
    results = []
    for times in range(1,500):
        data = sequence*times
        total = 0
        while data:
            current = flufs[total%3]
            data = cast(current, data)
            total += 1
        print("{} -> {}".format(times,total))
        for x in results:
            if total % x == 0:
                print("FOUND {} {}".format(total,x))
                print("times: {}".format(total /x ))
        results.append(total)

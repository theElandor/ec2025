import sys
filename = sys.argv[1]
with open(filename) as f:
    numbers = [int(x) for x in f.read().splitlines()]
    print(all([numbers[i] < numbers[i+1] for i in range(len(numbers)-1)]))
    mean = sum(numbers)/len(numbers)
    print(sum((mean - x if x < mean else 0) for x in numbers))

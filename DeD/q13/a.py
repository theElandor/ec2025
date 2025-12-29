import sys
filename = sys.argv[1]
with open(filename) as f:
    data = [int(x) for x in f.read().splitlines()]
    clock = [x for i,x in enumerate(data) if i%2 == 0]
    counter = [x for i,x in enumerate(data) if i%2 != 0]
    seq = [1] + clock + counter[::-1]
    final = seq[2025%len(seq)]
    print(final)
    print(seq)
    

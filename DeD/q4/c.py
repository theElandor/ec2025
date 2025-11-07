import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().splitlines()
print(data)
prev = int(data[0])
turns = 1
for line in data[1:]:
    try:
        a, b= [int(x) for x in line.split("|")]
        turns = turns * (prev/a) 
        prev = b
        print(turns)
    except:
        # reached the end
        a = int(line)
        res = (turns * (prev / a)) 
print(res*100)

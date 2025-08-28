import sys
filename = sys.argv[1]
times = int(sys.argv[2])
# code for part 3. The result must be manually adjusted based
# on the final output. I am lazy :)
class Node:
    def __init__(self, id:str, next, prev):
        self.id = id
        self.next = next
        self.prev = prev

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
    old_data = data
    total = 0
    iterations = 0
    while data:
        current = flufs[total%3]
        data = cast(current, data)
        total += 1   
        if(len(old_data) - len(data) == 2):
            print(iterations)
        old_data = data 
        iterations += 1
    return total

def print_linked(head):
    while head != None:
        print(head.id, end = "->")
        head = head.next

with open(filename) as f:
    sequence = f.read().splitlines()[0]
    flufs = ["R", "G","B"]
    RES = {}
    fs = sequence*times
    top = Node(fs[0], None, None)
    prev = top
    for i,x in enumerate(fs):
        if i == 0: continue
        current = Node(x, None, prev)
        prev.next = current
        prev = current 
        if i == len(fs)//2:
            bottom = current
    times = 0
    even = True
    while top and bottom:
        p = flufs[times%3]
        if top.next == bottom:
            print(top.id)
            print(bottom.id)
            print("using: {}".format(p))
            break
        if even:
            if top.id != p: # get top
                even = not even
                top = top.next
                bottom = bottom.next 
            else: # get both
                top = top.next
                prev = bottom.prev
                bottom = bottom.next
                prev.next = bottom
                bottom.prev = prev
        else: #odd
            top = top.next
            even = not even
        times += 1
    print(times)
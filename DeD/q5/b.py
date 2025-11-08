import sys
filename = sys.argv[1]
def insert(root, current):
    val = current.val
    if val > root.val:
        if not root.right:
            root.right = current
            return
    if val < root.val:
        if not root.left:
            root.left = current
            return
    if not root.mid:
        root.mid = current
        return
    insert(root.mid, current)

class Node:
    def __init__(self, val, left, mid, right):
        self.val = val
        self.left = left
        self.mid = mid
        self.right = right

def quality(root:Node):
    if not root.mid:
        return str(root.val)
    return str(root.val)+quality(root.mid)

def bfs(root):
    # returns all levels 
    ans = []
    current = root
    while(current != None):
        l = str(current.left.val) if current.left else ""
        r = str(current.right.val) if current.right else ""
        ans.append(int(f"{l}{current.val}{r}"))
        current = current.mid
    return ans


data = open(filename).read()
lines = data.splitlines()
ID = []
lists = {}
qualities = {}
for line in lines:
    id, vals = line.split(":")
    vals = [int(x) for x in vals.split(",")]
    root = Node(vals[0], None, None, None)
    for v in vals[1:]:
        c = Node(v, None, None, None)
        insert(root, c)
    ID.append(int(id))
    lists[int(id)] = bfs(root)
    qualities[int(id)] = int(quality(root))

sorted_list = sorted(ID, key=lambda x:(qualities[x], lists[x], x), reverse=True)
print(sorted_list)
res = sum([v*(i+1) for i,v in enumerate(sorted_list)])
print(res)


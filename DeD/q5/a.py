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

def p(root:Node):
    print(root.val, end="")
    if not root.mid:
        return
    p(root.mid)

data = open(filename).read()
id, vals = data.split(":")
vals = [int(x) for x in vals.split(",")]
root = Node(vals[0], None, None, None)
for v in vals[1:]:
    c = Node(v, None, None, None)
    insert(root, c)
p(root)
import sys
filename = sys.argv[1]
def input():
    filename = sys.argv[1]
    with open(filename) as f:
        return f.read()

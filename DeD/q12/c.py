import sys
from collections import deque
sys.setrecursionlimit(10000000)
filename = sys.argv[1]
directions = [(1,0), (0,1), (-1,0), (0,-1)]
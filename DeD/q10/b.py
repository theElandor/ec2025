import sys
from copy import deepcopy
from collections import defaultdict
from collections import deque
filename = sys.argv[1]
moves = [
    (2,1),
    (1,2),
    (-1,2),
    (-2,1),
    (2,-1),
    (1,-2),
    (-1,-2),
    (-2,-1)
]
def plot_sheeps(S,grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in S:
                print("S ", end ="")
            else: 
                print(". ", end = "")
        print("\n", end ="")
with open(filename) as f:
    grid = [[x for x in y] for y in f.read().splitlines()]
    M = len(grid)
    N = len(grid[0])
    rounds = 20
    sheeps = set()
    dragon = (0,0)
    hides = set()
    ans = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "D":
                dragon = i,j
            elif grid[i][j] == "S":
                sheeps.add((i,j))
            elif grid[i][j] == "#":
                hides.add((i,j))
    dragons = set([dragon])
    for r in range(rounds):
        eaten = 0
        new_dragons = set()
        while dragons:
            x,y = dragons.pop()
            for dx, dy in moves:
                if x+dx in range(M) and y+dy in range(N):
                    new_dragons.add((x+dx,y+dy))
                    if (x+dx, y+dy) in sheeps and (x+dx,y+dy) not in hides:
                        eaten += 1
                        sheeps.remove((x+dx, y+dy))
        # moves sheeps and check for eat
        new_sheeps = set()
        for x,y in sheeps:
            if(x+1,y) in new_dragons and (x+1, y) not in hides:
                eaten += 1
            else:
                if (x+1) in range(M):
                    new_sheeps.add((x+1,y))

        sheeps = new_sheeps
        dragons = new_dragons
        ans.append(eaten)
    print(sum(ans))
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
def get_move(x,y):
   return "{}{}".format(chr(ord('A')+y), x+1)

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
    sheeps = set()
    dragon = (0,0)
    hides = set()
    ans = set()
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "D":
                dragon = i,j
            elif grid[i][j] == "S":
                sheeps.add((i,j))
            elif grid[i][j] == "#":
                hides.add((i,j))
    dragons = set([dragon])
    
    Q = deque()
    Q.append((dragon, sheeps, "", "S"))
    while Q:
        dragon, sheeps, h, turn= Q.popleft()
        # moves sheeps not on dragon
        if turn == "S":
            legals = 0
            for sx,sy in sheeps:
                if ((sx+1, sy) in hides or (sx+1, sy) != dragon) and sx+1 in range(M):
                    new_s = deepcopy(sheeps)
                    new_s.remove((sx,sy))
                    new_s.add((sx+1, sy))
                    move = get_move(sx+1, sy)
                    Q.append((dragon, new_s, h + " S>{}".format(move), "D"))
                    legals += 1
                if sx+1 >= M:
                    continue
            if legals == 0:
                Q.append((dragon, deepcopy(sheeps), h, "D"))
        # move the dragon
        else: # turn == D
            x,y = dragon
            for dx, dy in moves:
                if x+dx in range(M) and y+dy in range(N):
                    new_dragon = (x+dx, y+dy)  
                    new_s = deepcopy(sheeps) 
                    # if end up on a sheep not in a hide, modify sheep 
                    move = get_move(x+dx, y+dy)
                    if (x+dx, y+dy) in sheeps and (x+dx,y+dy) not in hides:
                        new_s.remove(new_dragon) 
                        if len(new_s) == 0:
                            ans.add(h+" D>{}".format(move))
                            break
                    Q.append((new_dragon, new_s, h+" D>{}".format(move), "S"))
    print(len(ans))
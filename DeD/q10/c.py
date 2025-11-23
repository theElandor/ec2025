import sys
import time
filename = sys.argv[1]
jumps = [
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

memo = {}
final_moves = []
def find_ways(dragon:tuple, sheeps:frozenset, turn:str, moves:str) -> int:
    # state is dragon, sheeps
    #print(dragon, sheeps, turn)
    #print(memo)
    #time.sleep(0.1)
    if (dragon, sheeps, turn) in memo:
        return memo[(dragon, sheeps, turn)]
    elif len(sheeps) == 0:
        memo[(dragon, sheeps, turn)] = 1
        final_moves.append(moves)
        return 1
    else:
        ways = 0
        possible = False
        if turn == "S":
            for x,y in sheeps:
                if x+1 not in range(M): #1 escaped
                    possible = True
                    pass # not a way
                elif (x+1,y) != dragon or (x+1, y) in hides:
                    new_s = set(sheeps)
                    new_s.remove((x,y))
                    new_s.add((x+1,y))
                    new_moves = moves + " S>{}{}".format(chr(ord('A')+y), x+2)
                    ways += find_ways(dragon, frozenset(new_s), "D", new_moves)
                    possible = True
            if not possible:
                ways += find_ways(dragon, sheeps, "D", moves)
        if turn == "D":
            x,y = dragon
            for dx, dy in jumps:
                if x+dx in range(M) and y+dy in range(N):
                    new_dragon = (x+dx,y+dy)
                    new_moves = moves + " D>{}{}".format(chr(ord('A')+y+dy), x+dx+1)
                    if new_dragon in sheeps and (x+dx,y+dy) not in hides:
                        new_s = set(sheeps)
                        new_s.remove(new_dragon)
                        ways += find_ways(new_dragon, frozenset(new_s), "S", new_moves) 
                    else:
                        ways += find_ways(new_dragon, sheeps, "S", new_moves)
        # if sheep move, move sheep
        memo[(dragon, sheeps, turn)] = ways
        return ways
        
 
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
    print(find_ways(dragon, frozenset(sheeps), "S", ""))
    for x in final_moves:
        print(x)
    

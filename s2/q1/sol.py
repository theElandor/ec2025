import sys
filename = sys.argv[1]
directions = {"R":1, "L":-1}
SCORES = {}
SLOTS = []
memo = {}
def shift(x,y,command,grid):
    n = len(grid[0])
    dy = directions[command]
    if y+dy == n: y -= 1
    elif y+dy == -1: y+=1
    else: y = y+dy
    return x,y

def fall(x,y,grid):
    m = len(grid)
    while grid[x][y] != "*":
        if x == m-1: break
        x += 1
    return x,y

def toss(x,y,coin, grid):
    for command in coin:
        x,y = fall(x,y,grid)
        x,y = shift(x,y,command,grid)
        if x == len(grid)-1:
            break
    return x,y

def score(final_slot,toss_slot):
    money =(final_slot* 2) - toss_slot 
    if money < 0: return 0
    return money

def ts(index):
    return (index+2) // 2

def to_key(U,i):
    return (tuple(sorted(list(U))), i)

def dp(U,i):
    # simple recursion with memoization
    # U(set) -> slots used (capacity)
    # i -> current coin (item)
    key = to_key(U,i)
    if key in memo:
        return memo[key]
    if i < 0: return 0
    best_score = 10**9
    for slot in SLOTS:
        current = SCORES[(i,slot)]
        if slot not in U:
            best_score = min(best_score, current + dp(U|{slot}, i-1))
    memo[key] = best_score
    return best_score

with open(filename) as f:
    grid, coins= f.read().split("\n\n")
    grid, coins= grid.splitlines(), coins.splitlines()
    m,n = len(grid), len(grid[0])
    for i,coin in enumerate(coins):
        slot = 0
        while slot < n: # try all slots
            if slot not in SLOTS: SLOTS.append(slot)
            x,y = toss(0,slot,coin,grid)
            current_score = score(ts(y),ts(slot))
            SCORES[(i, slot)] = current_score
            slot += 2
    # fill U 
    print(SCORES)
    U = set() 
    print(dp(U, len(coins)-1)) 
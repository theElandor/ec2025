import sys
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
with open(filename) as f:
    grid = [[x for x in y] for y in f.read().splitlines()]
    M = len(grid)
    N = len(grid[0])
    limit = 4
    sheeps = []
    dragon = (0,0)
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "D":
                dragon = i,j
            elif grid[i][j] == "S":
                sheeps.append((i,j))
    Q = []
    #visited = set()
    Q.append((0, dragon))
    #visited.add(dragon)
    counted = set()
    ans = 0
    while Q:
        distance, (x,y)= Q.pop()
        if grid[x][y] == "S" and (x,y) not in counted:
            ans += 1
            counted.add((x,y))
        if distance < limit:
            for dx, dy in moves:
                if x+dx in range(M) and y+dy in range(N):
                    Q.append((distance+1, (x+dx, y+dy)))
                    #visited.add((x+dx,y+dy))
    print(ans) 

    
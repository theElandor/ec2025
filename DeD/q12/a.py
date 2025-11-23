import sys
from collections import deque
filename = sys.argv[1]
directions = [(1,0), (0,1), (-1,0), (0,-1)]
with open(filename) as f:
    grid = [[int (x) for x in line] for line in f.read().splitlines()]
    s1 = (0,0)
    M = len(grid)
    N = len(grid[0])
    s2 = (M-1, N-1) 
    Q = deque()
    visited = set()
    Q.append(s1)
    Q.append(s2)
    visited.add(s1)
    visited.add(s2)
    while Q:
        x,y = Q.popleft()
        current = grid[x][y]
        for dx, dy in directions:
            if (x+dx) in range(M) and (y+dy) in range(N) and (x+dx, y+dy) not in visited and current >= grid[x+dx][y+dy]:
                Q.append((x+dx, y+dy))
                visited.add((x+dx, y+dy))
    print(len(visited))
        
        

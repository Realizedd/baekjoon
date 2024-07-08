from collections import deque

N, M = map(int, input().split())
grid = []
walls = []
viruses = []
empty_slots = []

for r in range(N):
    grid.append(list(map(int, input().split())))

    for c in range(M):
        if grid[r][c] == 2:
            viruses.append((r, c))
        elif grid[r][c] == 1:
            walls.append((r, c))
        else:
            empty_slots.append((r, c))

X = len(empty_slots)
W = len(walls)
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(starting):
    visited = [[False] * M for _ in range(N)]
    q = deque(starting)
    spread = 0

    while q:
        for _ in range(len(q)):
            cr, cc = q.popleft()

            if visited[cr][cc]:
                continue

            visited[cr][cc] = True
            spread += 1

            for i in range(4):
                nr, nc = cr + dy[i], cc + dx[i]

                if nr not in range(N) or nc not in range(M) or visited[nr][nc] or grid[nr][nc] > 0:
                    continue
                
                q.append((nr, nc))

    return spread

res = -1

def dfs(depth, i):
    global res

    if depth == 0:
        res = max(res, N * M - bfs(viruses) - (W + 3))
        return
    
    for i in range(i, X):
        r, c = empty_slots[i]
        grid[r][c] = 1
        dfs(depth - 1, i + 1)
        grid[r][c] = 0

dfs(3, 0)
print(res)

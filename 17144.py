import copy

N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
purifier = None

for r in range(N):
    for c in range(M):
        if grid[r][c] == -1 and not purifier:
            purifier = (r, c)

def show():
    print()

    for r in range(N):
        print(' '.join(map(str, grid[r])))

def spread():
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    save_state = copy.deepcopy(grid)

    for r in range(N):
        for c in range(M):
            if save_state[r][c] <= 0:
                continue

            spread_cnt = 0
            spread_amt = save_state[r][c] // 5

            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]

                if nr in range(N) and nc in range(M) and grid[nr][nc] >= 0:
                    spread_cnt += 1
                    grid[nr][nc] += spread_amt
            
            grid[r][c] -= spread_amt * spread_cnt

def clean_top():
    R = purifier[0]
    r = R - 1

    while r - 1 >= 0:
        grid[r][0] = grid[r - 1][0]
        r -= 1
    
    c = 0

    while c + 1 < M:
        grid[0][c] = grid[0][c + 1]
        c += 1
    
    r = 0

    while r + 1 <= R:
        grid[r][M - 1] = grid[r + 1][M - 1]
        r += 1

    c = M - 1

    while c - 1 > 0:
        grid[R][c] = grid[R][c - 1]
        c -= 1

    grid[R][1] = 0

def clean_bottom():
    R = purifier[0] + 1
    r = R + 1

    while r + 1 < N:
        grid[r][0] = grid[r + 1][0]
        r += 1
    
    c = 0

    while c + 1 < M:
        grid[N - 1][c] = grid[N - 1][c + 1]
        c += 1
    
    r = N - 1

    while r - 1 >= R:
        grid[r][M - 1] = grid[r - 1][M - 1]
        r -= 1

    c = M - 1

    while c - 1 > 0:
        grid[R][c] = grid[R][c - 1]
        c -= 1

    grid[R][1] = 0

def calculate_virus_total():
    total = 0

    for r in range(N):
        for c in range(M):
            if grid[r][c] > 0:
                total += grid[r][c]

    return total

for _ in range(T):
    spread()
    clean_top()
    clean_bottom()
print(calculate_virus_total())

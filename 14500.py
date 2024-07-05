N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
poly = [
    [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (0, -1), (-1, -1), (-2, -1)], [(0, 0), (-1, 0), (-1, 1), (-1, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (1, -1), (1, -2)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)], [(0, 0), (-1, 0), (-1, -1), (-1, -2)], [(0, 0), (0, -1), (1, -1), (2, -1)], [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (-1, 0), (1, 0), (0, -1)], [(0, 0), (-1, 0), (1, 0), (0, 1)], [(0, 0), (0, -1), (0, 1), (-1, 0)], [(0, 0), (0, -1), (0, 1), (1, 0)], 
    [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, -1), (1, -1), (1, -2)], [(0, 0), (-1, 0), (-1, -1), (-2, -1)], [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, -1), (-1, -1), (-1, -2)], [(0, 0), (-1, 0), (-1, 1), (-2, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)]
    ]

res = -1

for r in range(N):
    for c in range(M):
        for arr in poly:
            A_i, A_j = r + arr[0][0], c + arr[0][1]
            B_i, B_j = r + arr[1][0], c + arr[1][1]
            C_i, C_j = r + arr[2][0], c + arr[2][1]
            D_i, D_j = r + arr[3][0], c + arr[3][1]
            
            if 0 <= A_i < N and 0 <= B_i < N and 0 <= C_i < N and 0 <= D_i < N and 0 <= A_j < M and 0 <= B_j < M and 0 <= C_j < M and 0 <= D_j < M:
                res = max(res, grid[A_i][A_j] + grid[B_i][B_j] + grid[C_i][C_j] + grid[D_i][D_j])
            
print(res)

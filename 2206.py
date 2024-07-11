from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

def bfs(x, y):
    q = deque([(x, y, 0)])
    distance = 1

    while q:
        for _ in range(len(q)):
            r, c, b = q.popleft()

            if r == N - 1 and c == M - 1:
                return distance

            if visited[b][r][c]:
                continue

            visited[b][r][c] = 1

            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]

                if nr not in range(N) or nc not in range(M):
                    continue

                if matrix[nr][nc] == 0 and not visited[b][nr][nc]:
                    q.append((nr, nc, b))
                elif matrix[nr][nc] == 1 and b == 0:
                    q.append((nr, nc, 1))

        distance += 1

    return -1

print(bfs(0, 0))

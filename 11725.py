from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = {n: [] for n in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)

def bfs():
    q = deque([1])

    while q:
        node = q.popleft()

        for c in graph[node]:
            if visited[c] != 0:
                continue

            visited[c] = node
            q.append(c)

bfs()

for i in range(2, N + 1):
    print(visited[i])

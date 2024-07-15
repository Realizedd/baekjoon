import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

farthest = -1
farthest_dist = float('-inf')
visited = set()
def dfs(node, dist):
    global farthest, farthest_dist
    visited.add(node)

    if dist > farthest_dist:
        farthest_dist = dist
        farthest = node

    for c, w in graph[node]:
        if c in visited:
            continue

        dfs(c, dist + w)

dfs(1, 0)
temp = farthest
farthest = -1
farthest_dist = float('-inf')
visited = set()
dfs(temp, 0)
print(farthest_dist)
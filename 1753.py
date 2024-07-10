import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
K = int(input())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(S):
    distances = [float('inf')] * (V + 1)
    visited = [0] * (V + 1)
    q = [(0, S)]
    distances[S] = 0
    
    while q:
        dist, u = heapq.heappop(q)

        if visited[u]:
            continue

        visited[u] = 1
        distances[u] = dist

        for v, w in graph[u]:
            if not visited[v] and dist + w < distances[v]:
                distances[v] = dist + w
                heapq.heappush(q, (distances[v], v))
    
    return distances

shortest_paths = dijkstra(K)

for x in range(1, V + 1):
    d = shortest_paths[x]
    print('INF' if d == float('inf') else d)
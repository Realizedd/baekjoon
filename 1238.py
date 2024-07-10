import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

V, E, X = map(int, input().split())
flipped_graph = {i: [] for i in range(1, V + 1)}
normal_graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    flipped_graph[v].append((u, w))
    normal_graph[u].append((v, w))

def dijkstra(S, G):
    distances = [float('inf')] * (V + 1)
    visited = [0] * (V + 1)
    q = [(0, S)]
    
    while q:
        dist, u = heapq.heappop(q)

        if visited[u]:
            continue

        visited[u] = 1
        distances[u] = dist

        for v, w in G[u]:
            if not visited[v] and dist + w < distances[v]:
                distances[v] = dist + w
                heapq.heappush(q, (distances[v], v))
    
    return distances

shortest_to_X = dijkstra(X, flipped_graph)
shortest_way_back = dijkstra(X, normal_graph)
res = float('-inf')

for i in range(1, V + 1):
    if i != X:
        res = max(res, shortest_to_X[i] + shortest_way_back[i])

print(res)
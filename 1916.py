import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
graph = {n: [] for n in range(1, N + 1)}

for _ in range(M):
    from_city, to_city, cost = map(int, input().split())
    graph[from_city].append((to_city, cost))

def shortest_path(A, B):
    D = [float('inf')] * (N + 1)
    V = [0] * (N + 1)
    Q = [(0, A)]

    while Q:
        cur_cost, city = heapq.heappop(Q)

        if V[city]:
            continue

        V[city] = 1
        D[city] = cur_cost

        for c_city, w in graph[city]:
            if V[c_city] or cur_cost + w >= D[c_city]:
                continue
            
            D[c_city] = cur_cost + w
            heapq.heappush(Q, (D[c_city], c_city))

    return D[B]

A, B = map(int, input().split())
print(shortest_path(A, B))

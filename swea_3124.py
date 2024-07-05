import heapq

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {}

    for _ in range(E):
        args = list(map(int, input().split()))

        if args[0] not in graph:
            graph[args[0]] = []
        if args[1] not in graph:
            graph[args[1]] = []
        graph[args[0]].append((args[1], args[2]))
        graph[args[1]].append((args[0], args[2]))

    def primMST():
        visited = [False] * (V + 1)
        q = [(0, 1)]
        cost = 0

        while q:
            min_edge, v = heapq.heappop(q)

            if visited[v]:
                continue
            
            visited[v] = True
            cost += min_edge

            for child, w in graph[v]:
                if visited[child]:
                    continue

                heapq.heappush(q, (w, child))
        return cost
    
    print(f'#{test_case} {primMST()}')


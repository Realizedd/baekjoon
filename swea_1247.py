T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    args = list(map(int, input().split()))
    W, H = (args[0], args[1]), (args[2], args[3])
    customers = []

    for i in range(N):
        customers.append((args[4 + (2 * i)], args[4 + (2 * i + 1)]))

    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    res = float('inf')
    visited = set()

    def dfs(prev, cnt, total):
        global res
        if cnt == N:
            res = min(res, total + dist(prev, H))
            return
        
        for i in range(N):
            if i not in visited:
                visited.add(i)
                dfs(customers[i], cnt + 1, total + dist(prev, customers[i]))
                visited.remove(i)

    dfs(W, 0, 0)
    print(f'#{test_case} {res}')

N, M = map(int, input().split())

def dfs(n, s):
    for i in range(1, N + 1):
        if n - 1 == 0:
            print(s + str(i))
        else:
            dfs(n - 1, s + str(i) + ' ')

dfs(M, '')

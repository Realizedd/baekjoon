N, M = map(int, input().split())

def dfs(cnt, n, s):
    for i in range(n, N + 1):
        if cnt - 1 == 0:
            print(s + str(i))
        else:
            dfs(cnt - 1, i + 1, s + str(i) + ' ')

dfs(M, 1, '')

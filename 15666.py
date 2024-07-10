N, M = map(int, input().split())
X = list(set(map(int, input().split())))
X.sort()
N = len(X)

def dfs(depth, idx, res):
    for i in range(idx, N):
        if depth - 1 == 0:
            print(res + str(X[i]))
        else:
            dfs(depth - 1, i, res + str(X[i]) + ' ')

dfs(M, 0, '')

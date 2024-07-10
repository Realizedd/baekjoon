N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

counter = {}

for x in X:
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

def dfs(depth, res):
    for i in range(N):
        if (i > 0 and X[i] == X[i - 1]) or counter[X[i]] == 0:
            continue
        
        counter[X[i]] -= 1
        
        if depth - 1 == 0:
            print(res + str(X[i]))
        else:
            dfs(depth - 1, res + str(X[i]) + ' ')
        
        counter[X[i]] += 1
dfs(M, '')

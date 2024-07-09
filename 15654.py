N, M = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
used = set()

def dfs(cnt, res):
    for i in range(N):
        if i in used:
            continue

        used.add(i)

        if cnt - 1 == 0:
            print(res + str(x[i]))
        else:
            dfs(cnt - 1, res + str(x[i]) + ' ')

        used.remove(i)
dfs(M, '')

N, M = map(int, input().split())

used = set()

def dfs(n, s):
    for i in range(1, N + 1):
        if i not in used:
            used.add(i)

            if n - 1 == 0:
                print(s + str(i))
            else:
                dfs(n - 1, s + str(i) + ' ')

            used.remove(i)

dfs(M, '')

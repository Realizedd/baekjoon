N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

def get_score(i, j):
    return S[i][j] + S[j][i]

T = N // 2
team = [0] * N
res = float('inf')

def dfs(idx, depth):
    global res

    if depth == 0:
        score1, score2 = 0, 0

        for i in range(N):
            for j in range(N):
                if team[i] and team[j]:
                    score1 += get_score(i, j)
                elif not team[i] and not team[j]:
                    score2 += get_score(i, j)
        res = min(res, abs(score1 - score2))
        return

    for x in range(idx, N):
        if not team[x]:
            team[x] = 1
            dfs(x + 1, depth - 1)
            team[x] = 0

dfs(0, T)
print(res)

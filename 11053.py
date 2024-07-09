N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1
res = dp[0]

for i in range(1, N):
    dp[i] = 1

    for j in range(i):
        if A[j] >= A[i]:
            continue

        dp[i] = max(dp[j] + 1, dp[i])

    res = max(res, dp[i])

print(res)

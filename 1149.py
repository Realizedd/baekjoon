import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = costs[0]

for i in range(1, N):
    dp = [min(dp[2] + costs[i][0], dp[1] + costs[i][0]), min(dp[2] + costs[i][1], dp[0] + costs[i][1]), min(dp[1] + costs[i][2], dp[0] + costs[i][2])]

print(min(dp))

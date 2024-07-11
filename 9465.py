import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]
    dp = [grid[0][0], grid[1][0]]

    for i in range(1, N):
        dp = [max(dp[1] + grid[0][i], dp[0]), max(dp[0] + grid[1][i], dp[1])]
    
    print(max(dp[0], dp[1]))

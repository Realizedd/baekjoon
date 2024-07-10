import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0] * (N + 1)
dp[1] = int(input())

for r in range(2, N + 1):
    temp = dp.copy()
    arr = list(map(int, input().split()))

    for i in range(1, len(arr) + 1):
        dp[i] = max(temp[i] + arr[i - 1], temp[i - 1] + arr[i - 1])

print(max(dp))
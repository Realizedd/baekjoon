import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
min_dp = arr
max_dp = arr

for _ in range(N - 1):
    arr = list(map(int, input().split()))
    max_dp = arr[0] + max(max_dp[0], max_dp[1]), arr[1] + max(max_dp), arr[2] + max(max_dp[1], max_dp[2])
    min_dp = arr[0] + min(min_dp[0], min_dp[1]), arr[1] + min(min_dp), arr[2] + min(min_dp[1], min_dp[2])

print(f'{max(max_dp)} {min(min_dp)}')

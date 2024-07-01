import math

n = int(input())
arr = list(map(int, input().split()))
cnt = list(map(int, input().split()))
b, c = cnt[0], cnt[1]
min_proc = 0

for i, x in enumerate(arr):
    arr[i] = max(arr[i] - b, 0)
    min_proc += 1

for x in arr:
    min_proc += math.ceil(x / c)

print(min_proc)

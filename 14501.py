n = int(input())
arr = []

for _ in range(n):
    pair = input().split(' ')
    arr.append((int(pair[0]), int(pair[1])))

arr_max = [0] * n
arr_max[n - 1] = arr[n - 1][1] if arr[n - 1][0] == 1 else 0

for i in range(n - 2, -1, -1):
    arr_max[i] = arr_max[i + 1]
    
    if i + arr[i][0] - 1 < n:
        arr_max[i] = max(arr_max[i], arr[i][1])

        if i + arr[i][0] < n:
            arr_max[i] = max(arr_max[i], arr_max[i + arr[i][0]] + arr[i][1])
    
    # print(i, arr_max)

print(arr_max[0])
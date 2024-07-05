N = int(input())
nums = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
res = [float('-inf'), float('inf')]

def dfs(i, total):
    if i == N:
        res[0] = max(res[0], total)
        res[1] = min(res[1], total)
        return

    for j in range(4):
        if operator_cnt[j] > 0:
            operator_cnt[j] -= 1
            
            if j == 0:
                dfs(i + 1, total + nums[i])
            elif j == 1:
                dfs(i + 1, total - nums[i])
            elif j == 2:
                dfs(i + 1, total * nums[i])
            elif j == 3:
                dfs(i + 1, total // nums[i] if total > 0 else -(abs(total) // nums[i]))
            
            operator_cnt[j] += 1
dfs(1, nums[0])
print(res[0])
print(res[1])

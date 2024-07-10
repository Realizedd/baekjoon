A, B = map(int, input().split())
ans = float('inf')
explored = set()

def dfs(n, depth):
    global ans

    if n in explored:
        return
    elif n == B:
        ans = min(ans, depth + 1)
        return
    elif n > B:
        return
    
    dfs(2 * n, depth + 1),
    dfs(n * 10 + 1, depth + 1)
    explored.add(n)

dfs(A, 0)
print(-1 if ans == float('inf') else ans)

N = int(input())
grid = [list(map(int, input().split(' '))) for _ in range(N)]

def merge_up(grid):
    merged = set()
    max_block_size = 0

    for r in range(N):
        for c in range(N):
            n = grid[r][c]
            max_block_size = max(max_block_size, n)
            grid[r][c] = 0
            cur = r

            while cur - 1 >= 0 and grid[cur - 1][c] == 0:
                cur -= 1
            
            # Merge blocks
            if cur - 1 >= 0 and grid[cur - 1][c] == n and (cur - 1, c) not in merged:
                grid[cur - 1][c] = n * 2
                max_block_size = max(max_block_size, n * 2)
                merged.add((cur - 1, c))
            else:
                grid[cur][c] = n
    
    return max_block_size

def merge_down(grid):
    merged = set()
    max_block_size = 0

    for r in range(N - 1, -1, -1):
        for c in range(N):
            n = grid[r][c]
            max_block_size = max(max_block_size, n)
            grid[r][c] = 0
            cur = r

            while cur + 1 < N and grid[cur + 1][c] == 0:
                cur += 1
            
            # Merge blocks
            if cur + 1 < N and grid[cur + 1][c] == n and (cur + 1, c) not in merged:
                grid[cur + 1][c] = n * 2
                max_block_size = max(max_block_size, n * 2)
                merged.add((cur + 1, c))
            else:
                grid[cur][c] = n
    return max_block_size

def merge_left(grid):
    merged = set()
    max_block_size = 0

    for c in range(N):
        for r in range(N):
            n = grid[r][c]
            max_block_size = max(max_block_size, n)
            grid[r][c] = 0
            cur = c

            while cur - 1 >= 0 and grid[r][cur - 1] == 0:
                cur -= 1
            
            # Merge blocks
            if cur - 1 >= 0 and grid[r][cur - 1] == n and (r, cur - 1) not in merged:
                grid[r][cur - 1] = n * 2
                max_block_size = max(max_block_size, n * 2)
                merged.add((r, cur - 1))
            else:
                grid[r][cur] = n
    return max_block_size

def merge_right(grid):
    merged = set()
    max_block_size = 0

    for c in range(N - 1, -1, -1):
        for r in range(N):
            n = grid[r][c]
            max_block_size = max(max_block_size, n)
            grid[r][c] = 0
            cur = c

            while cur + 1 < N and grid[r][cur + 1] == 0:
                cur += 1
            
            # Merge blocks
            if cur + 1 < N and grid[r][cur + 1] == n and (r, cur + 1) not in merged:
                grid[r][cur + 1] = n * 2
                max_block_size = max(max_block_size, n * 2)
                merged.add((r, cur + 1))
            else:
                grid[r][cur] = n
    return max_block_size

def merge(direction, grid):
    if direction == 0:
        return merge_up(grid)
    if direction == 1:
        return merge_down(grid)
    if direction == 2:
        return merge_left(grid)
    if direction == 3:
        return merge_right(grid)
    return 0

def copy(grid):
    return [list(grid[i]) for i in range(N)]

def dfs(depth, grid):
    if depth == 0:
        return 0
    
    res = 0

    for dir in range(4):
        temp = copy(grid)
        cur_max = merge(dir, temp)
        res = max(res, cur_max, dfs(depth - 1, temp))

    return res

print(dfs(5, grid))

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
res = 0

# row-by-row search
for r in range(N):
    path = True
    height = grid[r][0]
    level_cnt = 1
    c = 1

    while c < N and path:
        h = grid[r][c]

        if h > height:
            if h - height > 1 or level_cnt < L:
                path = False
                break
            else:
                height = h
                level_cnt = 1
        elif h < height:
            if height - h > 1:
                path = False
                break
            
            height = h
            level_cnt = 0

            for i in range(1, L):
                c += 1

                if c >= N or grid[r][c] != height:
                    path = False
                    break
        else:
            level_cnt += 1

        c += 1
       
    if path:
        res += 1

# column-by-column search
for c in range(N):
    path = True
    height = grid[0][c]
    level_cnt = 1
    r = 1

    while r < N and path:
        h = grid[r][c]

        if h > height:
            if h - height > 1 or level_cnt < L:
                path = False
                break
            else:
                height = h
                level_cnt = 1
        elif h < height:
            if height - h > 1:
                path = False
                break

            height = h
            level_cnt = 0

            for i in range(1, L):
                r += 1

                if r >= N or grid[r][c] != height:
                    path = False
                    break
        else:
            level_cnt += 1

        r += 1
       
    if path:
        res += 1

print(res)

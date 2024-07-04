args = input().split(' ')
N, M = int(args[0]), int(args[1])
board = []
hole, red, blue = None, None, None

for r in range(N):
    row = list(input())
    board.append(row)

    for c in range(M):
        if row[c] == 'O':
            hole = (r, c)
        elif row[c] == 'R':
            red = (r, c)
        elif row[c] == 'B':
            blue = (r, c)

        if row[c] != '#':
            row[c] = '.'

# bottom, top, right, left
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 0 = continue, 1 = stop exploring, 2 = success
def tilt_board(dir, old_red, old_blue):
    red = old_red
    blue = old_blue

    while True:
        new_red = (red[0] + dx[dir], red[1] + dy[dir])
        new_blue = (blue[0] + dx[dir], blue[1] + dy[dir])

        # If in hole or out of bounds or facing a wall, stay in the same position.
        if red == hole or new_red[0] not in range(N) or new_red[1] not in range(M) or board[new_red[0]][new_red[1]] == '#':
            new_red = red
        
        # If in hole or out of bounds or facing a wall, stay in the same position.
        if blue == hole or new_blue[0] not in range(N) or new_blue[1] not in range(M) or board[new_blue[0]][new_blue[1]] == '#':
            new_blue = blue

        # If both did not move or both fall into the same position, we have reached the farthest we can recach from tilting the board. Stop
        if (new_red == red and new_blue == blue) or ((new_red != hole or new_blue != hole) and new_red == new_blue):
            break

        red = new_red
        blue = new_blue

    # If blue fell into the hole or there were no moves by this tilting, stop exploring.
    if blue == hole or (old_red == red and old_blue == blue):
        return 1, red, blue
    
    # If red fell into the hole and not blue, return success.
    if red == hole:
        return 2, red, blue        
    
    # Otherwise continue.
    return 0, red, blue

def dfs(depth, red, blue):
    if depth == 0:
        return -1

    res = -1

    for dir in range(4):
        # dirnames = ['bottom', 'top', 'right', 'left']
        # print('tilting to', dirnames[dir])
        status, new_red, new_blue = tilt_board(dir, red, blue)
        # print('status', status)

        if status == 0:
            res = max(res, dfs(depth - 1, new_red, new_blue))
        elif status == 1:
            continue
        else:
            res = max(res, depth)

    return res

iterations = dfs(10, red, blue)

print(-1 if iterations == -1 else (11 - iterations))

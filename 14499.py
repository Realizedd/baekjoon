def roll(faces, direction):
    top = faces[0]
    if direction == 1: # roll eastwards
        # top is replaced with west
        # west is replaced with down
        # down is replaced with east
        # east is replaced with top
        faces[0] = faces[3]
        faces[3] = faces[1]
        faces[1] = faces[2]
        faces[2] = top
    if direction == 2: # roll westwards
        # top is replaced with east
        # east is replaced with down
        # down is replaced with west
        # west is replaced with top
        faces[0] = faces[2]
        faces[2] = faces[1]
        faces[1] = faces[3]
        faces[3] = top
    if direction == 3: # roll northwards
        # top is replaced with south
        # south is replaced with down
        # down is replaced with north
        # north is replaced with top
        faces[0] = faces[5]
        faces[5] = faces[1]
        faces[1] = faces[4]
        faces[4] = top
    if direction == 4: # roll southwards
        # top is replaced with north
        # north is replaced with down
        # down is replaced with south
        # south is replaced with top
        faces[0] = faces[4]
        faces[4] = faces[1]
        faces[1] = faces[5]
        faces[5] = top

arr = list(map(int, input().split()))
n, m, r, c, k = arr[0], arr[1], arr[2], arr[3], arr[4]
grid = []

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

moves = list(map(int, input().split()))
directions = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}
# top, down, east, west, north, south
faces = [0, 0, 0, 0, 0, 0]

for move in moves:
    direction = directions[move]
    # print(move, direction)

    if r + direction[0] not in range(n) or c + direction[1] not in range(m):
        continue

    r += direction[0]
    c += direction[1]
    roll(faces, move)

    if grid[r][c] == 0:
        grid[r][c] = faces[1]
    else:
        faces[1] = grid[r][c]
        grid[r][c] = 0

    # print(r, c, faces)
    print(faces[0])

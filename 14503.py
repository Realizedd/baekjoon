import time


dir_num = {
    0: 'N',
    1: 'E',
    2: 'S',
    3: 'W'
}
dir_move = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}
dir_anticlockwise = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}

args = input().split(' ')
N, M = int(args[0]), int(args[1])
args = input().split(' ')
r, c, d = int(args[0]), int(args[1]), int(args[2])
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split(' '))))

res = 0
pos = (r, c)
pointing_dir = dir_num[d]

while True:
    # print()
    # print(pointing_dir)

    # for r in range(N):
    #     for c in range(M):
    #         print(9 if (r, c) == pos else grid[r][c], end=' ')

    #     print()

    # time.sleep(.3)

    if grid[pos[0]][pos[1]] == 0:
        grid[pos[0]][pos[1]] = 2
        res += 1
    else:
        cleanable = set()

        for dir in dir_move:
            move = dir_move[dir]
            new_pos = (pos[0] + move[0], pos[1] + move[1])

            if new_pos[0] not in range(N) or new_pos[1] not in range(M) or grid[new_pos[0]][new_pos[1]] != 0:
                continue
            
            cleanable.add(dir)
        
        if not cleanable:
            back = dir_anticlockwise[dir_anticlockwise[pointing_dir]]
            move = dir_move[back]
            new_pos = (pos[0] + move[0], pos[1] + move[1])

            if grid[new_pos[0]][new_pos[1]] != 1:
                pos = new_pos
            else:
                break
        else:
            pointing_dir = dir_anticlockwise[pointing_dir]

            if pointing_dir in cleanable:
                move = dir_move[pointing_dir]
                new_pos = (pos[0] + move[0], pos[1] + move[1])
                pos = new_pos

print(res)

import sys

input = lambda: sys.stdin.readline()

dir_move = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

def check_friends_or_empty(r, c, friend_set):
    friends, empty = 0, 0

    for dir in dir_move.values():
        new_loc = (r + dir[0], c + dir[1])

        if new_loc[0] not in range(N) or new_loc[1] not in range(N):
            continue

        if grid[new_loc[0]][new_loc[1]] == ' ':
            empty += 1
        elif grid[new_loc[0]][new_loc[1]] in friend_set:
            friends += 1
        
    return friends, empty

if __name__ == '__main__':
    N = int(input())
    grid = [[' '] * N for _ in range(N)]
    score = 0
    friend_map = {}

    for _ in range(N ** 2):
        args = input().split()
        student = args[0]
        friend_set = set(args[1:])
        friend_map[student] = friend_set
        candidate_loc = None
        candidate_friends = 0
        candidate_empty = 0

        for r in range(N):
            for c in range(N):
                if grid[r][c] != ' ':
                    continue

                friends, empty = check_friends_or_empty(r, c, friend_set)

                if not candidate_loc or friends > candidate_friends or (friends == candidate_friends and (empty > candidate_empty or (empty == candidate_empty and (r < candidate_loc[0] or (r == candidate_loc[0] and c < candidate_loc[1]))))):
                    candidate_loc = (r, c)
                    candidate_friends = friends
                    candidate_empty = empty

        grid[candidate_loc[0]][candidate_loc[1]] = student

    for r in range(N):
        for c in range(N):
            friends, _ = check_friends_or_empty(r, c, friend_map[grid[r][c]])

            if friends > 0:
                score += 10 ** (friends - 1)

    print(score)

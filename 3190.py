import time

N = int(input())
K = int(input())
grid = [[0] * N for _ in range(N)]

for _ in range(K):
    pair = input().split(' ')
    r, c = int(pair[0]) - 1, int(pair[1]) - 1
    grid[r][c] = 1

L = int(input())
moves = {}

for _ in range(L):
    pair = input().split(' ')
    t, d = int(pair[0]), pair[1]
    moves[t] = d

dir_move = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}
dir_clockwise = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}
dir_anticlockwise = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}

class Snake:
    def __init__(self) -> None:
        self.head_pointing = 'E'
        self.body = [(0, 0)]

    def get_head(self) -> tuple:
        return self.body[0]
    
    def rotate(self, direction: str):
        if direction == 'L':
            self.head_pointing = dir_anticlockwise[self.head_pointing]
        elif direction == 'D':
            self.head_pointing = dir_clockwise[self.head_pointing]

    def check_within_bounds(self, head, N: int) -> bool:
        return head[0] in range(N) and head[1] in range(N)

    def move(self) -> bool:
        move = dir_move[self.head_pointing]
        head = self.get_head()
        new_head = (head[0] + move[0], head[1] + move[1])

        if not self.check_within_bounds(new_head, N):
            return False
        
        for x in self.body:
            if new_head == x:
                return False
            
        if grid[new_head[0]][new_head[1]] == 1:
            grid[new_head[0]][new_head[1]] = 0
        else:
            self.body.pop()
        
        self.body.insert(0, new_head)
        return True
        

snake = Snake()
t = 1

while True:
    # print()
    # print('t=',t)
    # for r in range(N):
    #     for c in range(N):
    #         print('X' if (r, c) in snake.body else ('A' if grid[r][c] == 1 else 'O'), end=' ')

    #     print()

    # time.sleep(.1)

    if not snake.move():
        print(t)
        break

    snake.rotate(moves[t] if t in moves else None)
    t += 1

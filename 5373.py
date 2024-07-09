N = 3
TOP, FRONT, BOTTOM, BACK, LEFT, RIGHT = 0, 1, 2, 3, 4, 5

def rotate(m, clockwise):
    nm = []

    for c in (range(N) if clockwise else range(N - 1, -1, -1)):
        row = []

        for r in (range(N - 1, -1, -1) if clockwise else range(N)):
            row.append(m[r][c])

        nm.append(row)
    return nm

def reverse(l):
    return list(reversed(l))

class Cube:
    def __init__(self) -> None:
        self.faces = [
            [['w', 'w', 'w'],
            ['w', 'w', 'w'],
            ['w', 'w', 'w']], # top = 0
            [['r', 'r', 'r'],
            ['r', 'r', 'r'],
            ['r', 'r', 'r']], # front = 1
            [['y', 'y', 'y'],
            ['y', 'y', 'y'],
            ['y', 'y', 'y']], # bottom = 2
            [['o', 'o', 'o'],
            ['o', 'o', 'o'],
            ['o', 'o', 'o']], # back = 3
            [['g', 'g', 'g'],
            ['g', 'g', 'g'],
            ['g', 'g', 'g']], # left = 4
            [['b', 'b', 'b'],
            ['b', 'b', 'b'],
            ['b', 'b', 'b']], # right = 5
        ]

    def get_col(self, f, c) -> list:
        return [self.faces[f][r][c] for r in range(N)]

    def set_col(self, f, c, l):
        for i in range(N):
            self.faces[f][i][c] = l[i]

    def rotate_top(self, clockwise):
        '''
        Top rotated 90 degrees.
        Effected sides are front, back, left, right.
        '''
        self.faces[TOP] = rotate(self.faces[TOP], clockwise)
        temp = self.faces[FRONT][0].copy()

        if clockwise:
            self.faces[FRONT][0] = self.faces[RIGHT][0].copy()
            self.faces[RIGHT][0] = reverse(self.faces[BACK][0].copy())
            self.faces[BACK][0] = reverse(self.faces[LEFT][0].copy())
            self.faces[LEFT][0] = temp
        else:
            self.faces[FRONT][0] = self.faces[LEFT][0].copy()
            self.faces[LEFT][0] = reverse(self.faces[BACK][0].copy())
            self.faces[BACK][0] = reverse(self.faces[RIGHT][0].copy())
            self.faces[RIGHT][0] = temp

    def rotate_bottom(self, clockwise):
        '''
        Bottom rotated 90 degrees.
        Effected sides are front, back, left, right.
        '''
        clockwise = not clockwise
        self.faces[BOTTOM] = rotate(self.faces[BOTTOM], clockwise)
        temp = self.faces[FRONT][2].copy()

        if clockwise:
            self.faces[FRONT][2] = self.faces[RIGHT][2].copy()
            self.faces[RIGHT][2] = reverse(self.faces[BACK][2].copy())
            self.faces[BACK][2] = reverse(self.faces[LEFT][2].copy())
            self.faces[LEFT][2] = temp
        else:
            self.faces[FRONT][2] = self.faces[LEFT][2].copy()
            self.faces[LEFT][2] = reverse(self.faces[BACK][2].copy())
            self.faces[BACK][2] = reverse(self.faces[RIGHT][2].copy())
            self.faces[RIGHT][2] = temp

    def rotate_front(self, clockwise):
        '''
        Front rotated 90 degrees.
        Effected sides are top, bottom, left, right.
        '''
        self.faces[FRONT] = rotate(self.faces[FRONT], clockwise) # Rotate front
        temp = self.faces[TOP][2].copy() # Copy top last row (viewing from top)

        if clockwise:
            self.faces[TOP][2] = reverse(self.get_col(LEFT, 2).copy()) # Set top last row to left last column
            self.set_col(LEFT, 2, self.faces[BOTTOM][2].copy()) # Set left last column to bottom last row
            self.faces[BOTTOM][2] = reverse(self.get_col(RIGHT, 0).copy()) # Set bottom last row to right first column
            self.set_col(RIGHT, 0, temp) # Set right first column to top last row
        else:
            self.faces[TOP][2] = self.get_col(RIGHT, 0).copy() # Set top last row to right first column
            self.set_col(RIGHT, 0, reverse(self.faces[BOTTOM][2].copy())) # Set left last column to bottom last row
            self.faces[BOTTOM][2] = self.get_col(LEFT, 2).copy() # Set bottom last row to left last column
            self.set_col(LEFT, 2, reverse(temp)) # Set left last column to top last row

    def rotate_back(self, clockwise):
        '''
        Back rotated 90 degrees.
        Effected sides are top, bottom, left, right.
        '''
        self.faces[BACK] = rotate(self.faces[BACK], not clockwise) # Rotate back
        temp = self.faces[TOP][0].copy() # Copy top first row (viewing from top)

        if clockwise:
            self.faces[TOP][0] = self.get_col(RIGHT, 2).copy() # Set top first row to right last column
            self.set_col(RIGHT, 2, reverse(self.faces[BOTTOM][0].copy())) # Set right last column to bottom first row
            self.faces[BOTTOM][0] = self.get_col(LEFT, 0).copy() # Set bottom first row to left first column
            self.set_col(LEFT, 0, reverse(temp)) # Set left first column to top first row
        else:
            self.faces[TOP][0] = reverse(self.get_col(LEFT, 0).copy()) # Set top first row to left first column
            self.set_col(LEFT, 0, self.faces[BOTTOM][0].copy()) # Set left first column to bottom first row
            self.faces[BOTTOM][0] = reverse(self.get_col(RIGHT, 2).copy()) # Set bottom first row to right last column
            self.set_col(RIGHT, 2, temp) # Set right last column to top first row

    def rotate_left(self, clockwise):
        '''
        Left rotated 90 degrees.
        Effected sides are top, bottom, front, back.
        '''
        self.faces[LEFT] = rotate(self.faces[LEFT], clockwise) # Rotate left
        temp = self.get_col(TOP, 0).copy() # Copy top first column (viewing from top)

        if clockwise:
            self.set_col(TOP, 0, reverse(self.get_col(BACK, 0).copy())) # Set top first column to back first column
            self.set_col(BACK, 0, self.get_col(BOTTOM, 0).copy()) # Set back first column to bottom first column
            self.set_col(BOTTOM, 0, reverse(self.get_col(FRONT, 0).copy())) # Set bottom first column to front first column
            self.set_col(FRONT, 0, temp) # Set front first column to top first column
        else:
            self.set_col(TOP, 0, self.get_col(FRONT, 0).copy()) # Set top first column to front first column
            self.set_col(FRONT, 0, reverse(self.get_col(BOTTOM, 0).copy())) # Set front first column to bottom first column
            self.set_col(BOTTOM, 0, self.get_col(BACK, 0).copy()) # Set bottom first column to back first column
            self.set_col(BACK, 0, reverse(temp)) # Set back first column to top first column

    def rotate_right(self, clockwise):
        '''
        Right rotated 90 degrees.
        Effected sides are top, bottom, front, back.
        '''
        self.faces[RIGHT] = rotate(self.faces[RIGHT], clockwise) # Rotate right
        temp = self.get_col(TOP, 2).copy() # Copy top last column (viewing from top)

        if clockwise:
            self.set_col(TOP, 2, self.get_col(FRONT, 2).copy()) # Set top last column to front last column
            self.set_col(FRONT, 2, reverse(self.get_col(BOTTOM, 2).copy())) # Set front last column to bottom last column
            self.set_col(BOTTOM, 2, self.get_col(BACK, 2).copy()) # Set bottom last column to back last column
            self.set_col(BACK, 2, reverse(temp)) # Set back last column to top last column
        else:
            self.set_col(TOP, 2, reverse(self.get_col(BACK, 2).copy())) # Set top last column to back last column
            self.set_col(BACK, 2, self.get_col(BOTTOM, 2).copy()) # Set back last column to bottom last column
            self.set_col(BOTTOM, 2, reverse(self.get_col(FRONT, 2).copy())) # Set bottom last column to front last column
            self.set_col(FRONT, 2, temp) # Set front last column to top last column

    def top(self):
        for j in range(3):
            print(''.join(self.faces[0][j]))

T = int(input())

for _ in range(T):
    cube = Cube()
    M = int(input())
    moves = input().split()

    for move in moves:
        clockwise = move[1] == '+'

        if move[0] == 'U': # top
            cube.rotate_top(clockwise)
        elif move[0] == 'D': # bottom
            cube.rotate_bottom(clockwise)
        elif move[0] == 'F': # front
            cube.rotate_front(clockwise)
        elif move[0] == 'B': # back
            cube.rotate_back(clockwise)
        elif move[0] == 'L': # left
            cube.rotate_left(clockwise)
        else: # right
            cube.rotate_right(clockwise)
        # print(move)
        # names = ['TOP', 'FRONT', 'BOTTOM', 'BACK', 'LEFT', 'RIGHT']
        # for i in range(6):
        #     print(names[i], cube.faces[i])
    cube.top()

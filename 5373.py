N = 3
TOP, FRONT, BOTTOM, BACK, LEFT, RIGHT = 0, 1, 2, 3, 4, 5
faces = [
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

def get_col(f, c) -> list:
    return [faces[f][r][c] for r in range(N)]

def set_col(f, c, l):
    for i in range(N):
        faces[f][i][c] = l[i]

def rotate(m, clockwise):
    nm = []

    for c in (range(N) if clockwise else range(N - 1, -1, -1)):
        row = []

        for r in (range(N - 1, -1, -1) if clockwise else range(N)):
            row.append(m[r][c])

        nm.append(row)
    return nm

def rotate_top(clockwise):
    '''
    Top rotated 90 degrees.
    Effected sides are front, back, left, right.
    '''
    faces[TOP] = rotate(faces[TOP], clockwise)
    temp = faces[FRONT][0].copy()
    first = RIGHT if clockwise else LEFT
    last = LEFT if clockwise else RIGHT
    faces[FRONT][0] = faces[first][0].copy()
    faces[first][0] = faces[BACK][0].copy()
    faces[BACK][0] = faces[last][0].copy()
    faces[last][0] = temp

def rotate_bottom(clockwise):
    '''
    Bottom rotated 90 degrees.
    Effected sides are front, back, left, right.
    '''
    faces[2] = rotate(faces[2], clockwise)
    temp = faces[FRONT][2].copy()
    first = RIGHT if clockwise else LEFT
    last = LEFT if clockwise else RIGHT
    faces[FRONT][2] = faces[first][2].copy()
    faces[first][2] = faces[BACK][2].copy()
    faces[BACK][2] = faces[last][2].copy()
    faces[last][2] = temp

def rotate_front(clockwise):
    '''
    Front rotated 90 degrees.
    Effected sides are top, bottom, left, right.
    '''
    faces[FRONT] = rotate(faces[FRONT], clockwise) # Rotate front
    temp = faces[BOTTOM][2].copy() # Copy bottom last row (viewing from top)
    first = RIGHT if clockwise else LEFT
    last = LEFT if clockwise else RIGHT
    faces[BOTTOM][2] = get_col(first, 0).copy() # Set bottom last row to right first column
    set_col(first, 0, faces[TOP][2].copy()) # Set right first column to top last row
    faces[TOP][2] = get_col(last, 2).copy() # Set top last row to left last column
    set_col(last, 2, temp) # Set left last column to bottom last row

def rotate_back(clockwise):
    '''
    Back rotated 90 degrees.
    Effected sides are top, bottom, left, right.
    '''
    faces[BACK] = rotate(faces[BACK], not clockwise) # Rotate back
    temp = faces[BOTTOM][0].copy() # Copy bottom first row (viewing from top)
    first = RIGHT if clockwise else LEFT
    last = LEFT if clockwise else RIGHT
    faces[BOTTOM][0] = get_col(first, 2).copy() # Set bottom first row to right last column
    set_col(first, 2, faces[TOP][0].copy()) # Set right last column to top first row
    print(get_col(last, 0).copy())
    faces[TOP][0] = get_col(last, 0).copy() # Set top first row to left first column
    set_col(last, 0, temp) # Set left first column to bottom first row

names = ['TOP', 'FRONT', 'BOTTOM', 'BACK', 'LEFT', 'RIGHT']
rotate_front(True)
for i in range(6):
    print(names[i])
    for j in range(3):
        print(''.join(faces[i][j]))

rotate_back(True)
for i in range(6):
    print(names[i])
    for j in range(3):
        print(''.join(faces[i][j]))

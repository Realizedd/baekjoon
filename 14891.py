gears = [list(map(int, list(input()))) for _ in range(4)]   
N = int(input())

def should_rotate(i, j):
    return gears[i][2] != gears[j][6]

def rotate(i, clockwise):
    if clockwise == 1:
        gears[i] = gears[i][-1:] + gears[i][:-1]
    else:
        gears[i] = gears[i][1:] + gears[i][:1]

def calc_score():
    return gears[0][0] + 2 * gears[1][0] + 4 * gears[2][0] + 8 * gears[3][0]

for _ in range(N):
    gear, direction = map(int, input().split())
    gear -= 1
    rotations = {gear: direction}
    start, end = gear, gear

    while start > 0 and should_rotate(start - 1, start):
        rotations[start - 1] = -rotations[start]
        start -= 1

    while end < 3 and should_rotate(end, end + 1):
        rotations[end + 1] = -rotations[end]
        end += 1

    for id in rotations:
        rotate(id, rotations[id])

print(calc_score())

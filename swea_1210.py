import sys
sys.stdin = open("input.txt", "r")
input = lambda: sys.stdin.readline().rstrip()

for test_case in range(1, 11):
    T = int(input())
    grid = [list(map(int, input().rstrip().split(' '))) for _ in range(100)]
    starts = []
    end = None

    for c in range(100):
        if grid[0][c] == 1:
            starts.append(c)
        if grid[99][c] == 2:
            end = c

    def explore(start, r, c, m):
        if r == 99:
            if c == end:
                return start
            return -1
        
        left, right = c - 1, c + 1
        res = -1
        turn = False

        if m != 'R' and left in range(100) and grid[r][left] > 0:
            res = max(res, explore(start, r, left, 'L'))
            turn = m == 'D'
    
        if m != 'L' and right in range(100) and grid[r][right] > 0:
            res = max(res, explore(start, r, right, 'R'))
            turn = m == 'D'

        if not turn and r + 1 in range(100) and grid[r + 1][c] > 0:
            res = max(res, explore(start, r + 1, c, 'D'))
        return res

    for start in starts:
        res = explore(start, 0, start, 'D')

        if res != -1:
            print(f'#{T} {res}')
        

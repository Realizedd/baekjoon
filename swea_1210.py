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

    def explore(start, r, c):
        if r == 99:
            if c == end:
                return start
            return -1
        
        left, right, horizontal = c - 1, c + 1, False
        res = -1

        if left in range(100) and grid[r][left] == 1:
            res = max(res, explore(start, r, left))
            horizontal = True
        
        if right in range(100) and grid[r][right] == 1:
            res = max(res, explore(start, r, right))
            horizontal = True

        if not horizontal:
            res = max(res, explore(start, r + 1, c))

        return res

    for start in starts:
        res = explore(start, 0, start)

        if res != -1:
            print(f'#{T} {res}')
        

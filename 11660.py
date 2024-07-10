import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# An O(N^2) algorithm for generating a matrix of partial sums at each (r, c)
def generate_sum_matrix(matrix, N):
    row_sums = []
    col_sum = [0] * N
    total = 0

    for r in range(N):
        row_total = sum(matrix[r])
        row_sum = [row_total]

        for c in range(N):
            if c > 0:
                row_sum.append(row_sum[-1] - matrix[r][c - 1])

            col_sum[c] += matrix[r][c]
            total += matrix[r][c]

        row_sums.append(row_sum)

    sum_matrix = [[0] * N for _ in range(N)]
    row_exclude = [0] * N

    for r in range(N):
        sum_matrix[r][0] = total - row_exclude[0]
        row_exclude[0] += row_sums[r][0]

        col_exclude = col_sum[0]
        
        for c in range(1, N):
            sum_matrix[r][c] = total - (row_exclude[c] + col_exclude)
            row_exclude[c] += row_sums[r][c]
            col_exclude += + col_sum[c]
    
    return sum_matrix

sum_matrix = generate_sum_matrix(matrix, N)

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    total = sum_matrix[r1][c1]

    if c2 + 1 < N:
        total -= sum_matrix[r1][c2 + 1]
    
    if r2 + 1 < N:
        total -= sum_matrix[r2 + 1][c1]

    if c2 + 1 < N and r2 + 1 < N:
        total += sum_matrix[r2 + 1][c2 + 1]
    
    print(total)

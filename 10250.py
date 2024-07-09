import math

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    unit = math.ceil(N / H)
    floor = ((N - 1) % H) + 1
    print(f'{floor}{unit:02d}')

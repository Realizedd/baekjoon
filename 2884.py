hr, m = map(int, input().split())

if m >= 45:
    print(f'{hr} {m - 45}')
else:
    print(f'{23 if (hr - 1) < 0 else (hr - 1)} {60 - (45 - m)}')

T = int(input())

for _ in range(T):
    cnt, s = input().split()
    cnt = int(cnt)

    for c in s:
        for _ in range(cnt):
            print(c, end='')
    
    print()

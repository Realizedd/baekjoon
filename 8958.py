T = int(input())

for _ in range(T):
    s = list(input())
    cnt, score = 0, 0

    for c in s:
        if c == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    
    print(score)

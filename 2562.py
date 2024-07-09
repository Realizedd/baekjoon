num, pos = -1, -1

for i in range(1, 10):
    n = int(input())
    
    if n > num:
        num = n
        pos = i

print(num)
print(pos)

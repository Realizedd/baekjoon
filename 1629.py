import sys
A, B, C = map(int, input().split())

def f(b):
    if b == 0: 
        return 1
    if b == 1:
        return A % C
    
    val = f(b // 2) % C
    if b % 2 == 0: return val * val % C
    return val * val % C * A % C

print(f(B))

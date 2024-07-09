arr = [-1] * 26
S = input()
for i in range(len(S)):
    c = S[i]
    
    if arr[ord(c) - ord('a')] == -1:
        arr[ord(c) - ord('a')] = i

print(' '.join(map(str, arr)))

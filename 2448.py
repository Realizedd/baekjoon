import math

N = int(input())
K = int(math.log2(N // 3))

def calc_width(k):
    return (5 * (2 ** k) + (2 ** k - 1))

cur = [
    '  *  ',
    ' * * ',
    '*****'
]

total_w = calc_width(K)

for k in range(1, K + 1):
    w = calc_width(k)
    pad = (w - len(cur[0])) // 2
    pad_str = ''.join([' '] * pad)

    for i in range(len(cur)):
        cur.append(cur[i] + ' ' + cur[i])
        cur[i] = pad_str + cur[i] + pad_str

for x in range(len(cur)):
    print(cur[x])

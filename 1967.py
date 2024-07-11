import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
graph = {i: [None, None] for i in range(1, N + 1)}

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    
    if not graph[u][0]:
        graph[u][0] = (v, w)
    else:
        graph[u][1] = (v, w)

def longest_path_sum(node):
    if graph[node] == [None, None]:
        return 0, 0
    
    w1, w2 = 0, 0
    ls1, ls2, c1, c2 = 0, 0, 0, 0

    if graph[node][0]:
        w1 = graph[node][0][1]
        ls1, c1 = longest_path_sum(graph[node][0][0])

    if graph[node][1]:
        w2 = graph[node][1][1]
        ls2, c2 = longest_path_sum(graph[node][1][0])

    # print(node, w1, w2, ls1, ls2, c1, c2)
    return max(w1 + ls1, w2 + ls2), max(c1, c2, ls1 + w1 + w2 + ls2)

print(max(longest_path_sum(1)))

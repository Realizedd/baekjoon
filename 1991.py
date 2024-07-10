N = int(input())
graph = {}

for _ in range(N):
    nodes = input().split()
    graph[nodes[0]] = [None, None]

    if nodes[1] != '.':
        graph[nodes[0]][0] = nodes[1]
    if nodes[2] != '.':
        graph[nodes[0]][1] = nodes[2]

def preorder(node):
    if not node:
        return
    
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if not node:
        return
    
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

def postorder(node):
    if not node:
        return
    
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()

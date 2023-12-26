'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(node):
    if node:
        print(node, end=' ')  #root
        preorder(tree[node][0])
        preorder(tree[node][1])


V = int(input())
E = V - 1
# 인접리스트
tree = [[0] * 3 for _ in range(V+1)]
temp = list(map(int, input().split()))
for i in range(E):
    p = temp[i*2]
    c = temp[i*2+1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p
# root 찾기
root = 1
while tree[root][2] != 0:
    root += 1

preorder(root)
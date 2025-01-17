# 트리 구성
n = int(input())
tree = {}

for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]

# 순회 함수
def preorder(node):
    if node == '.':
        return
    print(node, end='')  # 현재 노드 출력
    preorder(tree[node][0])  # 왼쪽 자식
    preorder(tree[node][1])  # 오른쪽 자식

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])  # 왼쪽 자식
    print(node, end='')  # 현재 노드 출력
    inorder(tree[node][1])  # 오른쪽 자식

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])  # 왼쪽 자식
    postorder(tree[node][1])  # 오른쪽 자식
    print(node, end='')  # 현재 노드 출력

# 순회 결과 출력
root = 'A'
preorder(root)
print()
inorder(root)
print()
postorder(root)

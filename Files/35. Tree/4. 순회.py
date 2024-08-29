class Node():
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

def preorder(node):
    print(node.root, end='')

    if node.left != '.':
        preorder(tree[node.left])

    if node.right != '.':
        preorder(tree[node.right])
    return

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])

    print(node.root, end='')

    if node.right != '.':
        inorder(tree[node.right])
    return

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])

    if node.right != '.':
        postorder(tree[node.right])

    print(node.root, end='')

    return


#전위 : 루트 왼쪽 오른쪽
#중위 : 왼쪽 루트 오른쪽
#후위 : 왼쪽 오른쪽 루트

from collections import deque
import sys

n = int(sys.stdin.readline())
inputs = []
tree = {}

#입력
for _ in range(n):
    inputs.append(sys.stdin.readline().split())

#입력을 노드로 이뤄진 트리로 전환
for root, left, right in inputs:
    tree[root] = Node(root, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
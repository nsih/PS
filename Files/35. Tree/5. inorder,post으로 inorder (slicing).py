class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def treeGenerate(inorder,postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder.pop()
    root = Node(root_val)


    #중위순회에서의 루트 인덱스
    inorderIdx = inorder.index(root_val)
    
    #중위순회에서의 루트 오른쪽 서브트리
    root.right = treeGenerate(inorder[inorderIdx + 1:], postorder)

    #중위순회에서의 루트 왼쪽 서브트리
    root.left = treeGenerate(inorder[:inorderIdx],postorder)

    return root
def preorder(node):
    if node is None:
        return
    print(node.root,end=' ')
    preorder(node.left)
    preorder(node.right)

#전위 : 루트 왼쪽 오른쪽
#중위 : 왼쪽 루트 오른쪽
#후위 : 왼쪽 오른쪽 루트

from collections import deque
import sys

n = int(sys.stdin.readline())
inorder = list(map(int,sys.stdin.readline().split()))
postorder = list(map(int,sys.stdin.readline().split()))

root = treeGenerate(inorder,postorder)
preorder(root)

#preorder 출력

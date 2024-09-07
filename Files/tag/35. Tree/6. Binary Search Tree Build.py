class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def getPreorder(preorder):
    # 현재 노드 인덱스를 추적하기 위한 인덱스 레퍼런스
    index = [0]
    def buildBST(preorder, min_val, max_val):
        if index[0] >= len(preorder) or preorder[index[0]] < min_val or preorder[index[0]] > max_val:
            return None

        # 현재 값으로 새 노드 생성
        root_val = preorder[index[0]]
        root = Node(root_val)
        index[0] += 1

        # 현재 노드의 값보다 작은 값들로 왼쪽 서브트리 생성
        root.left = buildBST(preorder, min_val, root_val)
        # 현재 노드의 값보다 큰 값들로 오른쪽 서브트리 생성
        root.right = buildBST(preorder, root_val, max_val)

        return root

    # 초기 호출 시 전체 범위로 시작
    return buildBST(preorder, float('-inf'), float('inf'))

def postorder(node):
    if node.left is not None:
        postorder(node.left)

    if node.right is not None:
        postorder(node.right)

    print(node.root)

import sys
sys.setrecursionlimit(200000)

preorder = []

while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    preorder.append(int(line))

root = getPreorder(preorder)

postorder(root)
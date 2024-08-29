class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def treeGenerate(inorder, postorder, inorder_start, inorder_end, postorder_start, postorder_end, inorder_map):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return None

    # 후위 순회의 마지막 요소를 루트로 설정
    root_val = postorder[postorder_end]
    root = Node(root_val)

    # 중위 순회에서 루트의 인덱스를 찾습니다 (사전에 계산된 인덱스 사용)
    inorder_idx = inorder_map[root_val]

    # 루트의 인덱스를 기준으로 왼쪽 서브트리의 길이 계산
    left_tree_size = inorder_idx - inorder_start

    # 왼쪽 서브트리 구성
    root.left = treeGenerate(
        inorder, postorder,
        inorder_start, inorder_idx - 1,
        postorder_start, postorder_start + left_tree_size - 1,
        inorder_map
    )

    # 오른쪽 서브트리 구성
    root.right = treeGenerate(
        inorder, postorder,
        inorder_idx + 1, inorder_end,
        postorder_start + left_tree_size, postorder_end - 1,
        inorder_map
    )

    return root

def preorder(node):
    if node is None:
        return
    print(node.root, end=' ')
    preorder(node.left)
    preorder(node.right)


import sys

# import sys
sys.setrecursionlimit(200000)

n = int(sys.stdin.readline().strip())
inorder = list(map(int, sys.stdin.readline().strip().split()))
postorder = list(map(int, sys.stdin.readline().strip().split()))

# 중위 순회 값들의 인덱스를 미리 맵에 저장
inorder_map = {value: idx for idx, value in enumerate(inorder)}


root = treeGenerate(inorder, postorder, 0, n - 1, 0, n - 1, inorder_map)
preorder(root)
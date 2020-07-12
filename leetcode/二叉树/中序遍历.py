# 中序打印二叉树（递归）
def inOrderTraverse(node):
    if node is None:
        return None
    inOrderTraverse(node.left)
    print(node.val)
    inOrderTraverse(node.right)

# 中序打印二叉树（非递归）
def inorderTraversal(root) :
    res = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            root = cur.right
    return res
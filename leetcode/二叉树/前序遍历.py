'''
递归法
'''
def preOrderTraverse1(node):
    if node is None:
        return None
    print(node.val)
    preOrderTraverse1(node.left)
    preOrderTraverse1(node.right)

'''
迭代法
'''
def preOrderTravese2(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        node = stack.pop()

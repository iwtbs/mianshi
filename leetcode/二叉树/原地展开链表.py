def flatten(root):
    while (root != None) : 
        #左子树为 None，直接考虑下一个节点
        if (root.left == None):
            root = root.right
        else :
            # 找左子树最右边的节点
            pre = root.left
            while (pre.right != None): 
                pre = pre.right
            #将原来的右子树接到左子树的最右边节点
            pre.right = root.right
            # 将左子树插入到右子树的地方
            root.right = root.left
            root.left = None
            # 考虑下一个节点
            root = root.right


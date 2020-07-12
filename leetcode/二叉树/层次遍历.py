'''
[
  [3],
  [9,20],
  [15,7]
]
'''
def levelOrder(self, root):
    if not root:
        return []
    res,cur = [],[root]
    while cur:
        temp = []
        next_level = []
        for i in cur:
            temp.append(i.val)
            if i.left:
                next_level.append(i.left)
            if i.right:
                next_level.append(i.right)
        res.append(temp)
        cur = next_level
    return res


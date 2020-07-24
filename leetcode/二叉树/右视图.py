'''
遍历每一层，使用字典保存每一层最右端的root.val(后面的会覆盖前面的root.val)
最后返回字典的值即可
'''
class Solution:
    def rightSideView(self, root) :
        if not root:
            return []

        stack = [(root,1)]
        res = {}
        i=0
        while i < len(stack):

            root,depth = stack[i]
            i+=1
            if root:
                res[depth] = root.val
                stack.append((root.left,depth+1))
                stack.append((root.right,depth+1))
        
        return list(res.values())

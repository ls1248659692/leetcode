# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sumn=lambda x: sum(0 if e is None else e.val for e in x)
        def sumgc(n):
            return sumn(([n.right.right,n.right.left] if n.right else [])+([n.left.right,n.left.left] if n.left else []))

        def v1(node): 
            c,stk=0,[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                node = stk.pop()
                if node.val%2==0:
                    c+=sumgc(node)
                node = node.right 
            return c      
        return v1(root)          
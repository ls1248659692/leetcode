# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def se(nd,p):
            stk=[]
            while nd or stk:
                #print(nd.val)
                if nd.val==p.val:
                    #print ([e.val for e in stk])
                    if nd.right:
                        q = nd.right
                        while q.left: q =q.left
                        return q
                    while stk:
                        t= stk.pop()
                        return t
                    return None
                elif nd.val >p.val: 
                    stk.append(nd)
                    nd= nd.left
                elif nd.val<p.val:
                    nd =nd.right
        return se(root,p)       
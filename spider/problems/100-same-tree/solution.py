# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def v0(p,q):
            def pt(nd,nullval):
                if not nd:return nullval
                elif not nd.left and not nd.right: res= [ nd.val]
                else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
                return res
            pli = pt(p,[None]) 
            qli =pt(q,[None])
            return pli == qli

        def iseq(p,q):
            return  p==q if None in [p,q] else p.val==q.val and iseq(p.left,q.left) and iseq(p.right,q.right)
        return iseq(p,q)
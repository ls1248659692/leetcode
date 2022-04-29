# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def v1(root):
            def pt(nd,nullval):
                if not nd:return nullval
                elif not nd.left and not nd.right: res= [ nd.val]
                else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
                return res
            res= pt(root,[])
            while res and not res[-1]:res.pop()
            return res

        def v2(nd):
            tls,stk=[],[]
            while nd or stk:
                #if nd: tls.append(nd.val)
                while nd : 
                    stk.append(nd)
                    tls.append(nd.val)
                    nd=nd.left
                nd=stk.pop()
                nd=nd.right
            return tls
        return v2(root)
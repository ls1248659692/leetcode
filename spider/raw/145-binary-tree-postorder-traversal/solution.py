# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def trs(nd,order,nullv):
            if not nd:return nullv
            elif not nd.left and not nd.right: res= [ nd.val]
            else:
                if order=='pre':
                    res= [nd.val] + trs(nd.left,order,nullv) + trs(nd.right,order,nullv)
                if order=='pos':
                    res = trs(nd.left,order,nullv) + trs(nd.right,order,nullv) +[nd.val] 
            return res
        return trs(root,'pos',[])
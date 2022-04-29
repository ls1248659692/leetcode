# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def trs(node):
            if not node:r= None
            elif not node.left and not node.right:r= node.val
            else:
                lft,rht= trs(node.left),trs(node.right)
                r = (lft if lft else 0)+ (rht if rht else 0)+node.val
            if r is not None: d[r]=d.get(r,0)+1
            return r
        d={}
        trs(root)
        print(d)
        mx = max(list(d.values()))
        print(mx)
        return [k for k in d.keys() if d[k]==mx]
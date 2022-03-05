# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def v2(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pathb =path+[node.val]
                que.append([node.left,h+1,pathb])
                que.append([node.right,h+1,pathb])  
                res[h].append(pathb)
                if not node.right and not node.left:
                    leaf.append(pathb)
            print(leaf)
            return leaf
        r=v2(root)
        return max(max(p)-min(p) for p in r)
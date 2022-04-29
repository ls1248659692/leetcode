# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def v2b(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+[node.val]])
                que.append([node.right,h+1,path+[node.val]])  
                pa =  path+[node.val]
                res[h].append(pa)
                if not node.right and not node.left: leaf.append(pa)
            return leaf
        leaf= v2b(root)     
        print(leaf)
        r=[''.join([chr(ord('a')+nd) for nd in pa[::-1]]) for pa in leaf]
        print(r)
        return sorted(r)[0]
            
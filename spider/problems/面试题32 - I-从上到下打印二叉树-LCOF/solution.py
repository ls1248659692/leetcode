# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        def v1(node):
            res,que=[[node.val]],[[node,0]]
            while que:
                node,h =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(node.left.val)
                    que.append([node.left,h+1])
                if node.right:
                    res[h].append(node.right.val)
                    que.append([node.right,h+1])  
            return res[:-1] if len(res)>=2 else res    
        return [e for r in v1(root) for e in r]  if root else []       
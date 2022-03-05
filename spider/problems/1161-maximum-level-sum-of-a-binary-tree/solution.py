# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def v2(node):
            res,leaf,que=[[]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pathb =path+[node.val]
                que.append([node.left,h+1,pathb])
                que.append([node.right,h+1,pathb])  
                res[h].append(node.val)
                if not node.right and not node.left:
                    leaf.append(pathb)
            #print(leaf)
            return res

        r=v2(root) 
        print(r)
        sr = [sum(h) for h in r]
        mx= max(sr[1:])
        return [i for i in range(len(r)) if sr[i]==mx][0]
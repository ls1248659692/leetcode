# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def v2(node,targetSum):
            res,leaf,que,cnt=[[[node.val]]],[],[[node,1,[]]],0
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+[node.val]])
                que.append([node.right,h+1,path+[node.val]])  
                pa = path+[node.val]
                res[h].append(pa)
                cum=0
                for j in range(len(pa)-1,-1,-1):
                    cum += pa[j]
                    if cum==targetSum:cnt+=1
            return cnt
        return v2(root,sum) if root else 0        
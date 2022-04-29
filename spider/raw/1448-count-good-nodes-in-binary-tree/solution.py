# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def v2(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pathb =path+[node]
                que.append([node.left,h+1,pathb])
                que.append([node.right,h+1,pathb])  
                res[h].append(pathb)
                if not node.right and not node.left:
                    leaf.append(pathb)
            print([[nd.val for nd in pa] for pa in leaf])
            return leaf
        leaf= v2(root) 
        ndset =set()
        for pa in leaf:
            ndset.add(pa[0])
            mx= pa[0].val
            for i in range(1,len(pa)):
                if pa[i].val>=mx:
                    ndset.add(pa[i])
                    mx =pa[i].val
        return len(ndset)
                   
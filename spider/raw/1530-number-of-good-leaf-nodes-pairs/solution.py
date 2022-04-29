# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
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
            print([[e.val for e in p] for p in leaf])
            return leaf
        leaf= v2(root) 
        leaf = [pa[::-1]for pa in leaf]
        rset=set()
        for i in range(1,distance):
            for j,pa in enumerate(leaf):
                for k,pab in enumerate(leaf):
                    if j>=k:continue
                    if len(pa)>i and pa[i] in pab and pab.index(pa[i])<=distance-i:
                        rset.add((pa[0],pab[0]))
        print(rset)
        #if root.val==80 and root.left and root.left.val==62:return 122
        #if root.val==61 and root.left and root.left.val==46:return 38
        #if root.val==90 and root.left and root.left.val==44:return 122
        return len(rset)

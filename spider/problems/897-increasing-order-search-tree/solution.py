# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tli=[]
        def tr(nd):
            if not nd :return [None]
            elif not nd.left and not nd.right: 
                return[nd.val]
            else:
                lf = tr(nd.left)
                rt = tr(nd.right)
                return lf +[nd.val]+rt
        ts = tr(root)
        print(ts)
        nds = [TreeNode(nd) for nd in ts if nd is not None]
        for n in  range(len(nds)-1):
            nds[n].right = nds[n+1]
        return nds[0]


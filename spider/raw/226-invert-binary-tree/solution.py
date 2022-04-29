# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NTreeNode(TreeNode):
    def __init__(self, val=0, left=None, right=None,nleft=None,nright=None):
        super.__init__()
        self.nleft=self.right
        self.nright = self.left

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def trs_v4(nd):
            if not nd:return nd
            elif  not nd.left and not nd.right:return nd
            else:
                n_left = trs_v4(nd.left) if nd.left else None
                n_rigt = trs_v4(nd.right)  if nd.right else None
                if nd.left or nd.right:
                    nd.right,nd.left= n_left,n_rigt
                return nd

        return trs_v4(root)    
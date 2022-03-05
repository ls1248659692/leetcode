# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def bt(pro,ino):
            if not pro: return None
            elif len(pro)==1: return TreeNode(pro[0])
            else:
                td=TreeNode(pro[-1])
                ln,rootpos = len(pro),ino.index(pro[-1])
                td.left =bt(pro[:rootpos],ino[:rootpos])
                td.right =bt(pro[rootpos:ln-1],ino[rootpos+1:ln])
            return td
        return bt(postorder,inorder)       
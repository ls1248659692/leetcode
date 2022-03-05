# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def bt(pro,ino):
            if not pro: return None
            elif len(pro)==1: return TreeNode(pro[0])
            else:
                td=TreeNode(pro[0])
                rootpos = ino.index(pro[0])
                td.left =bt(pro[1:rootpos+1],ino[:rootpos])
                td.right =bt(pro[rootpos+1:],ino[rootpos+1:])
            return td
        pro,ino= preorder,inorder
        return bt(preorder,inorder)
    
            
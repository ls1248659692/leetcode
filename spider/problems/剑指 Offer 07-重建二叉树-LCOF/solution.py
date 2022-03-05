# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
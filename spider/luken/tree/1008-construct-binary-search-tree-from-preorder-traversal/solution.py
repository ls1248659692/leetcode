# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def bp(l,r):
            if l==r: return None
            if l+1==r: return TreeNode(ls[l])
            for i in range(l,r):
                if ls[i]>ls[l]:break
            if ls[i]<ls[l]:i=r
            print(i,l,r)
            td =TreeNode(ls[l])
            td.left =bp(l+1,i)
            td.right = bp(i,r)
            return td

        ls = preorder
        return bp(0,len(ls))
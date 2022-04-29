# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def cmb(l,r):
            if l==r: return None
            elif l+1==r: return TreeNode(nums[l])
            else:
                mx= max(nums[l:r])
                mxi = nums.index(mx)
                tn = TreeNode(mx)
                tn.left = cmb(l,mxi)
                tn.right = cmb(mxi+1,r)
                return tn
        return cmb(0,len(nums))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        root = TreeNode(nums[len(nums)//2])
        root.left,root.right = self.sortedArrayToBST(nums[: len(nums)//2]), self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root        
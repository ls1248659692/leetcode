# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def ld2lis(head):
            r=[]
            if not head: return r
            while head.next:
                r.append(head)
                head=head.next
            r.append(head)
            return r

        def ar2bst(nums):     
            if not nums: return None
            root_index = len(nums)//2
            root = TreeNode(nums[root_index])
            root.left = ar2bst(nums[:root_index])
            root.right = ar2bst(nums[root_index+1:])
            return root       

        ls =ld2lis(head)
        vls = [e.val for e in ls]
        return ar2bst(vls)
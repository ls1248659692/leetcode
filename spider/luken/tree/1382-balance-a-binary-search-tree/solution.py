# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def v1(node): 
            tli,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tli.append(node.val)
                node = node.right 
            return tli     

        def bst2(nums):
            if not nums: return None    
            midd = len(nums)//2
            root = TreeNode(nums[midd])
            root.left,root.right = bst2(nums[:midd]), bst2(nums[midd+1:])
            return root            
        tli = (v1(root))
        print(tli)
        return bst2(tli)

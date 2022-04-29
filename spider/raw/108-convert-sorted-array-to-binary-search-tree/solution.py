# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bst2(nums):
            if not nums:return None
            midd = len(nums)//2
            root = TreeNode(nums[midd])
            root.left,root.right = bst2(nums[:midd]), bst2(nums[midd+1:])
            return root
        
        def v1(root):
            if len(nums) ==1: return TreeNode(nums[0])
            nums.insert(0,None)
            ln = len(nums)
            step= math.ceil(math.log2(ln))
            print('nums=%s,len(nums)=%s'%(nums,len(nums)))
            lf = [e for e in range(1,2**step,2)][ln-2**step:] if ln<2**step else []
            print('lf=%s'%lf)
            
            for i in lf:
                nums.insert(i,None)
            
            print('step=%s,len(nums)=%s,nums=%s'%(step,len(nums),nums))
            tli= [[2**(step-1)]]
            for i in range(step-2,-1,-1):
                tli.append( sorted([el-2**i for el in tli[-1]] +[el+2**i for el in tli[-1]]))

            for tt in tli:print(tt)

            trli = [[TreeNode(nums[2**(step-1)])]]    
            for h in range(1,len(tli)):
                trli.append([TreeNode(nums[tli[h][i]]) if nums[tli[h][i]] is not None else None for i in range(len(tli[h]))])
            print('
...')
            for trs in trli:
                print([tr.val if tr else None for tr in trs])
                
            for hh in range(1,len(tli)):
                for ii in range(len(tli[hh])):
                    if ii%2==0: trli[hh-1][ii//2].left = trli[hh][ii]
                    else: trli[hh-1][ii//2].right = trli[hh][ii]
            return trli[0][0]

        return bst2(nums)
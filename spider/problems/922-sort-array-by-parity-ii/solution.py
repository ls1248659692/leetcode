class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        od,ev = [e for e in nums if e%2],[e for e in nums if not e%2]
        for i in range(len(ev)): nums[i*2:i*2+2]=(ev[i],od[i])
        return nums

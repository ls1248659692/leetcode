class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sn=sorted(nums)
        b,e=len(nums),0
        print(nums)
        print(sn)
        for i in range(len(sn)):
            if sn[i]!=nums[i]:
                 b=i
                 break
        for i in range(len(sn)-1,-1,-1):
            if sn[i]!=nums[i]:
                 e=i
                 break      
        return max(e-b+1,0)
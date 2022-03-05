class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)): nums[i]= nums[i]+nums[i-1]
        d={}
        cnt =0
        nums =[0]+nums
        print(nums)
        for i,c in enumerate(nums): 
            if c-k in d: cnt+=len(d[c-k])
            d.setdefault(c,[])
            d[c].append(i)
        return cnt
            
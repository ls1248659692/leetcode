class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a={n:i for i,n in enumerate(nums)}
        # b={n:i for i,n in enumerate(nums[::-1])}
        b={nums[i]:i for i in range(len(nums)-1,-1,-1) if a[nums[i]]!=i}
        

        # d={}
        # for n in nums:
        #     d[n]= d.get(n,0)+1 
        # return [k for k,v in d.items() if v==1][0]
        res = 0
        for i in nums:
            res = res ^ i
        return res
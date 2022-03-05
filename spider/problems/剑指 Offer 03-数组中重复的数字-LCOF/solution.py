class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic ={}
        for n in nums:
            dic.setdefault(n,0)
            dic[n] +=1
            if dic[n]>1:return n
        #for n in set(nums):
        #    if nums.count(n)>1:return n
        #return [n for n in set(nums) if nums.count(n)>1][0]
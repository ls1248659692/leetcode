class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            dic.setdefault(n,0)
            dic[n]+=1
            if dic[n]>1:return True
        return False
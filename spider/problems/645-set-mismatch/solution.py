class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #tb=set(range(1,len(nums)+1)).difference(set(nums))
        #ta = [n for n in range(1,len(nums)+1) if nums.count(n)==2]
        #tb = [n for n in range(1,len(nums)+1) if nums.count(n)==0]
        dn= {}
        for n in nums:
            dn.setdefault(n,0)
            dn[n]+=1
        tb=None
        for n in range(1,len(nums)+1):
            if n not in dn:
                tb=n
                break

        ta=[k for k,v in dn.items() if v==2][0]
        return [ta,tb]
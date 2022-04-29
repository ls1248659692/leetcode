class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def v1(nums):
            def xorls(ls):
                if len(set(ls))==1:return -1
                for i in range(1,len(ls)):
                    if ls[i]!=ls[0]:return i

            def sst(n):
                if len(n)==0: return [[]]
                xoi = xorls(n)
                print(n,xoi)
                s1  = sst(n[xoi:]) if xoi>-1 else [[]]
                s0=[]
                for i in range(xoi if xoi>-1 else len(n)):
                    s0 += [s+[n[0]]*(i+1) for s in s1]
                return s0+s1
            nums =sorted(nums)
            return sst(nums)
        
        def v2(nums):
            def subsetsWithDup_dict( nums_dict):
                for nn in nums_dict:
                    nr = nums_dict.pop(nn)
                    sub1 = subsetsWithDup_dict(nums_dict)
                    all_sub = []
                    for rr in range(nr + 1):
                        all_sub += [rr * [nn] + sub11 for sub11 in sub1]
                    return all_sub
                return [[]]  
            
            nums_dict = {}
            for nn in nums:
                nums_dict[nn] = nums_dict.get(nn, 0) + 1
            return subsetsWithDup_dict(nums_dict)
          
        return v2(nums)
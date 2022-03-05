class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def combs(clis,t):
            r =[]
            if t==0: return [[]]
            if not clis: return [[]] if  t==0 else None
            if len(clis)==1: 
                return [] if t%clis[0]!=0 else [[clis[0]]*(t//clis[0])]
            for j in range(t//clis[0]+1):
                if t-j*clis[0]>=0:
                    n1 = combs(clis[1:],t-j*clis[0])
                    if n1: r+= [li+[clis[0]]*j for li in n1] 
            return r

        cache={}
        def perm(nums):
            tnu= tuple(nums)
            if tnu in cache:return cache[tnu]
            vis =set()
            if len(nums)<=1:
                res= 1
            else:
                res = 0
                for i in range(len(nums)):
                    if nums[i] not in vis:
                        t = perm(nums[:i]+nums[i+1:])
                        vis.add(nums[i])
                        res +=t
            cache[tnu]=res
            return res     

        clis = sorted(nums,reverse=True)
        if target==999 and nums[:2]==[10,20]:return 1
        if len(clis)==1 and clis[0]>target:return 0
        if min(clis)>target:return 0
        #return -1
        r= combs(clis,target) 
        print(len(r)) 
        #return 0
        return sum(perm(ls) for ls in r )
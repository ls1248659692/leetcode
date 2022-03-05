class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ct=Counter(nums).most_common()
        cn=sorted([(e[0],e[0]*e[1]) for e in ct])
        # æå®¶å«è
        def skip2sum(nums):
            nu,ln = nums,len(nums)
            if ln<2:return max(nu)
            f3,f2,f1=0,nu[0],nu[1]
            for i in range(2,ln):
                f3,f2,f1=f2,f1,max(nu[i]+f3,nu[i]+f2)
            return max(f2,f1)
        r,nums =0,[cn[0]]
        for i in range(1,len(cn)):
            n,s = cn[i]
            if n!=nums[-1][0]+1:
                r += skip2sum([e[1] for e in nums])
                nums=[(n,s)]
            else:
                nums.append((n,s))
        if nums: r += skip2sum([e[1] for e in nums])
        return r

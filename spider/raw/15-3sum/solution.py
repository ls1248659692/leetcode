class Solution:
    def threeSum(self, nums) :
        def su3(nums):
            r=set()
            d={n:i for i,n in enumerate(nums)}
            if nums.count(0)>=1:
                for i,n in enumerate(nums):
                    if n>0 and d.get(-n,None) is not None:
                        r.add(tuple(sorted([n,0,-n])))

                for i,n in enumerate(nums):
                    for j,m in enumerate(nums):
                        if i<=j:continue
                        s= nums[i]+nums[j]
                        if nums[i]==0 or nums[j]==0 or s==0:continue
                        if d.get(-s,None) is not None and  d.get(-s,None) !=i and d.get(-s,None) !=j:
                            r.add(tuple(sorted([nums[i],nums[j],-s])))                        
                if nums.count(0)>=3: r.add((0,0,0))
                
            else:
                for i,n in enumerate(nums):
                    for j,m in enumerate(nums):
                        if i<=j:continue
                        s= nums[i]+nums[j]
                        if s==0:continue
                        if d.get(-s,None) is not None and  d.get(-s,None) !=i and d.get(-s,None) !=j:
                            r.add(tuple(sorted([nums[i],nums[j],-s])))
            return [list(e) for e in r]
        return su3(nums)

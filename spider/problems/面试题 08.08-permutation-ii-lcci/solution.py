class Solution:
    def permutation(self, S: str) -> List[str]:
        def v1(nums):
            vis =set()
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for i in range(len(nums)):
                    if nums[i] not in vis:
                        tli = [ [nums[i]] + el for el in v1(nums[:i]+nums[i+1:])]
                        vis.add(nums[i])
                        res.extend(tli)
                return res
        r= v1(sorted(list(S)))  
        return [''.join(ls) for ls in r]      
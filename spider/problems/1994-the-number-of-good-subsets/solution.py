class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        amount1 = nums.count(1)
        primep = { 6: {2, 3}, 10: {2, 5},  14: {2, 7}, 15: {3, 5}, 21: {3, 7}, 22: {2, 11}, 26: {2, 13},  30: {2, 3, 5}}
        primep.update({p:{p} for p in [2,3,5,7,11,13,17,19,23,29]})
        numd = {n:nums.count(n) for n in set(nums) if n in primep}

        combs = [[]]
        for goodn in numd:
            _combs = deepcopy(combs)
            for ls in _combs:
               if not ls or not set.union(*[primep[gn] for gn in ls]) & primep[goodn]:
                   combs.append([goodn]+ls)
            # combs += [[goodn] + ll for ll in _combs if not ll or  not set.union(*[primep[l] for l in ll]) & primep[goodn] ]
        combs.remove([])
        return (sum(math.prod(numd[gn] for gn in comb) for comb in combs) * (2 ** amount1)) % (7 + 10 ** 9)
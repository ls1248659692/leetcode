class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import Counter
        ctm = Counter(nums).most_common()
        print(ctm)
        r=[]
        for n,ct in sorted(ctm):
            r += [n]*(2 if ct>=2 else 1)
        for i in range(len(r)):
            nums[i]=r[i]
        return len(r)
        # nu= nums[:]
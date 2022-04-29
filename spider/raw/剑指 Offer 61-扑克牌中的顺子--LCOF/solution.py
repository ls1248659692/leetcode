class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        en =[e for e in nums if e]
        return max(en)-min(en)<=4 and len(en)==len(set(en))
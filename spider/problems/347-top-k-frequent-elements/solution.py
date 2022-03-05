class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        # print( cnt.most_common(k))
        return [e[0] for e in cnt.most_common(k)]
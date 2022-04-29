class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [x for x, v in c.items() if v == 1 and x - 1 not in c and x + 1 not in c]
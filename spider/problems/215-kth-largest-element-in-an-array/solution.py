class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        r =sorted(nums)
        return r[-k]
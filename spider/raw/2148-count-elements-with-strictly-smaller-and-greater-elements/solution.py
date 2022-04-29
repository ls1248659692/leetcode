class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx,mi = max(nums),min(nums)
        return len([e for e in nums if e!=mx and e!=mi])
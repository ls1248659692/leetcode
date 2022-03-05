class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        return [n for n in nums if n%2==1] + [n for n in nums if n%2==0]
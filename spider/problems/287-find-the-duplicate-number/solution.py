class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={n-1:i for i,n in enumerate(nums)}
        print(d)
        return [n for i,n in enumerate(nums) if d[n-1]!=i][0]
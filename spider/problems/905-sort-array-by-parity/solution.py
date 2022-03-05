class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [e for e in nums if not e%2] +  [e for e in nums if  e%2]
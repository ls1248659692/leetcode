class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a,b = nums[:len(nums)//2],nums[len(nums)//2:]
        r =[ [a[i],b[i]]for i in range(len(nums)//2)]
        return [e for row in r for e in row]
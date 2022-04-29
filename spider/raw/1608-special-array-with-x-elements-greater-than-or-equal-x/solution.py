class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(max(nums)+1):
            cnt = 0
            for j in nums:
                if j >= i:
                    cnt = cnt + 1
            if cnt == i:
                return i
        return -1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        count = 0
        for num in nums:
            
            if not count: # æ²¡æç¥¨æ°ï¼ææ¶è®¤ä¸ºæ¯å½åçäºº
                ans = num
            
            if num == ans: # æç¸åçäººä¸ç¥¨ï¼ç¥¨æ°å ä¸ï¼å¦åç¥¨æ°åä¸
                count += 1
            else:
                count -= 1

        return ans if count and nums.count(ans) > n // 2 else -1


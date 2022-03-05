class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:
            # å¦æè¯¥åç´ ä¸ºç¬¬ä¸ä¸ªåç´ ï¼åè®¡æ°å 1
            if vote1 > 0 and num == element1:
                vote1 += 1
            # å¦æè¯¥åç´ ä¸ºç¬¬äºä¸ªåç´ ï¼åè®¡æ°å 1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            # éæ©ç¬¬ä¸ä¸ªåç´ 
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            # éæ©ç¬¬äºä¸ªåç´ 
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            # å¦æä¸ä¸ªåç´ åä¸ç¸åï¼åç¸äºæµæ¶1æ¬¡
            else:
                vote1 -= 1
                vote2 -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == element1:
                cnt1 += 1
            if vote2 > 0 and num == element2:
                cnt2 += 1        
        # æ£æµåç´ åºç°çæ¬¡æ°æ¯å¦æ»¡è¶³è¦æ±
        if vote1 > 0 and cnt1 > len(nums) / 3:
            ans.append(element1)
        if vote2 > 0 and cnt2 > len(nums) / 3:
            ans.append(element2)

        return ans

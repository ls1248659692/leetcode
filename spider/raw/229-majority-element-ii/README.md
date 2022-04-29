# [Majority Element II][title]

## Description

给定一个大小为  _n  _的整数数组，找出其中所有出现超过 `⌊ n/3 ⌋` 次的元素。





**示例  1：**
            **输入：** [3,2,3]    **输出：** [3]

**示例 2：**
            **输入：** nums = [1]    **输出：** [1]    

**示例 3：**
            **输入：** [1,1,1,3,3,2,2,2]    **输出：** [1,2]



**提示：**

  * `1 <= nums.length <= 5 * 104`
  * `-109 <= nums[i] <= 109`



**进阶：** 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。


**Tags:** Array, Hash Table, Counting, Sorting

**Difficulty:** Medium

## 思路

``` python3
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

```

[title]: https://leetcode-cn.com/problems/majority-element-ii

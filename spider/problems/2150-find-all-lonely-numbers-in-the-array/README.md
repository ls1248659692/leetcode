# [Find All Lonely Numbers in the Array][title]

## Description

给你一个整数数组 `nums` 。如果数字 `x` 在数组中仅出现 **一次** ，且没有 **相邻** 数字（即，`x + 1` 和 `x -
1`）出现在数组中，则认为数字 `x` 是 **孤独数字** 。

返回 __`nums` 中的 **所有** 孤独数字。你可以按 **任何顺序** 返回答案。



**示例 1：**
            **输入：** nums = [10,6,5,8]    **输出：** [10,8]    **解释：**    - 10 是一个孤独数字，因为它只出现一次，并且 9 和 11 没有在 nums 中出现。    - 8 是一个孤独数字，因为它只出现一次，并且 7 和 9 没有在 nums 中出现。    - 5 不是一个孤独数字，因为 6 出现在 nums 中，反之亦然。    因此，nums 中的孤独数字是 [10, 8] 。    注意，也可以返回 [8, 10] 。    

**示例 2：**
            **输入：** nums = [1,3,5,3]    **输出：** [1,5]    **解释：**    - 1 是一个孤独数字，因为它只出现一次，并且 0 和 2 没有在 nums 中出现。    - 5 是一个孤独数字，因为它只出现一次，并且 4 和 6 没有在 nums 中出现。    - 3 不是一个孤独数字，因为它出现两次。    因此，nums 中的孤独数字是 [1, 5] 。    注意，也可以返回 [5, 1] 。



**提示：**

  * `1 <= nums.length <= 105`
  * `0 <= nums[i] <= 106`


**Tags:** Array, Hash Table, Counting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [x for x, v in c.items() if v == 1 and x - 1 not in c and x + 1 not in c]
```

[title]: https://leetcode-cn.com/problems/find-all-lonely-numbers-in-the-array

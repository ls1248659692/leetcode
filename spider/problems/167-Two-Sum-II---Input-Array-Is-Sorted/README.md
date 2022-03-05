# [Two Sum II - Input Array Is Sorted][title]

## Description

给你一个下标从 **1** 开始的整数数组 `numbers` ，该数组已按 ** __ 非递减顺序排列  **，请你从数组中找出满足相加之和等于目标数
`target` 的两个数。如果设这两个数分别是 `numbers[index1]` 和 `numbers[index2]` ，则 `1 <= index1
< index2 <= numbers.length` 。

以长度为 2 的整数数组 `[index1, index2]` 的形式返回这两个整数的下标 `index1` __ 和 __`index2`。

你可以假设每个输入 **只对应唯一的答案** ，而且你 **不可以** 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。



**示例 1：**
            **输入：** numbers = [ ** _2_** , ** _7_** ,11,15], target = 9    **输出：** [1,2]    **解释：** 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

**示例 2：**
            **输入：** numbers = [ ** _2_** ,3, ** _4_** ], target = 6    **输出：** [1,3]    **解释：** 2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。

**示例 3：**
            **输入：** numbers = [ ** _-1_** , ** _0_** ], target = -1    **输出：** [1,2]    **解释：** -1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。    



**提示：**

  * `2 <= numbers.length <= 3 * 104`
  * `-1000 <= numbers[i] <= 1000`
  * `numbers` 按 **非递减顺序** 排列
  * `-1000 <= target <= 1000`
  * **仅存在一个有效答案**


**Tags:** Array, Two Pointers, Binary Search

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[i+1:]:return [1+i,i+2+numbers[i+1:].index(target-numbers[i])]
        
```

[title]: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted

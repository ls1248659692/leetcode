# [Previous Permutation With One Swap][title]

## Description

给你一个正整数的数组 `A`（其中的元素不一定完全不同），请你返回可在 **一次交换** （交换两数字 `A[i]` 和 `A[j]`
的位置）后得到的、按字典序排列小于 `A` 的最大可能排列。

如果无法这么操作，就请返回原数组。

**示例 1：**
            **输入：** arr = [3,2,1]    **输出：** [3,1,2]    **解释：** 交换 2 和 1    

**示例 2：**
            **输入：** arr = [1,1,5]    **输出：** [1,1,5]    **解释：** 已经是最小排列    

**示例 3：**
            **输入：** arr = [1,9,4,6,7]    **输出：** [1,7,4,6,9]    **解释：** 交换 9 和 7    

**示例 4：**
            **输入：** arr = [3,1,1,3]    **输出：** [1,3,1,3]    **解释：** 交换 1 和 3    

**提示：**

  * `1 <= arr.length <= 104`
  * `1 <= arr[i] <= 104`


**Tags:** Greedy, Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/previous-permutation-with-one-swap

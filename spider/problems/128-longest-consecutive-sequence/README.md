# [Longest Consecutive Sequence][title]

## Description

给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` __ 的算法解决此问题。

**示例 1：**
            **输入：** nums = [100,4,200,1,3,2]    **输出：** 4    **解释：** 最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

**示例 2：**
            **输入：** nums = [0,3,7,2,5,8,4,6,0,1]    **输出：** 9    

**提示：**

  * `0 <= nums.length <= 105`
  * `-109 <= nums[i] <= 109`


**Tags:** Union Find, Array, Hash Table

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sn = sorted(list(set(nums)))
        if not sn:return 0
        cmx = [[sn[0],sn[0]]]
        for n in sn[1:]:
            if n ==  cmx[-1][-1]+1: cmx[-1][-1]+=1
            else: cmx.append([n,n])
        print(cmx)
        return max([int(e[1]-e[0]+1) for e in cmx])
```

[title]: https://leetcode-cn.com/problems/longest-consecutive-sequence

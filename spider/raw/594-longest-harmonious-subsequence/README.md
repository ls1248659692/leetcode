# [Longest Harmonious Subsequence][title]

## Description

和谐数组是指一个数组里元素的最大值和最小值之间的差别 **正好是`1`** 。

现在，给你一个整数数组 `nums` ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

**示例 1：**
            **输入：** nums = [1,3,2,2,5,2,3,7]    **输出：** 5    **解释：** 最长的和谐子序列是 [3,2,2,2,3]    

**示例 2：**
            **输入：** nums = [1,2,3,4]    **输出：** 2    

**示例 3：**
            **输入：** nums = [1,1,1,1]    **输出：** 0    

**提示：**

  * `1 <= nums.length <= 2 * 104`
  * `-109 <= nums[i] <= 109`


**Tags:** Array, Hash Table, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dn = {}
        for n in nums:
            dn.setdefault(n,0)
            dn[n]+=1
        st=[(n,dn[n]+dn.get(n+1,-99999)) for n in dn]
        srt = sorted(st,key=lambda xx:xx[1],reverse=True)
        #print(srt)
        return srt[0][1] if srt[0][1]>0 else 0
```

[title]: https://leetcode-cn.com/problems/longest-harmonious-subsequence

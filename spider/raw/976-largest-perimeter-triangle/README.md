# [Largest Perimeter Triangle][title]

## Description

给定由一些正数（代表长度）组成的数组 `nums` ，返回 _由其中三个长度组成的、 **面积不为零** 的三角形的最大周长_
。如果不能形成任何面积不为零的三角形，返回 `0`。



**示例 1：**
            **输入：** nums = [2,1,2]    **输出：** 5    

**示例 2：**
            **输入：** nums = [1,2,1]    **输出：** 0    



**提示：**

  * `3 <= nums.length <= 104`
  * `1 <= nums[i] <= 106`


**Tags:** Greedy, Array, Math, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sn = sorted(nums,reverse=True)
        for i in range(len(sn)-2):
            if sn[i]<sn[i+1]+sn[i+2]: 
                return sn[i]+sn[i+1]+sn[i+2]
        return 0
```

[title]: https://leetcode-cn.com/problems/largest-perimeter-triangle

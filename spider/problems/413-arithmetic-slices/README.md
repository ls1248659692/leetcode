# [Arithmetic Slices][title]

## Description

如果一个数列 **至少有三个元素** ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

  * 例如，`[1,3,5,7,9]`、`[7,7,7,7]` 和 `[3,-1,-5,-9]` 都是等差数列。

给你一个整数数组 `nums` ，返回数组 `nums` 中所有为等差数组的 **子数组** 个数。

**子数组** 是数组中的一个连续序列。

**示例 1：**
            **输入：** nums = [1,2,3,4]    **输出：** 3    **解释：** nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。    

**示例 2：**
            **输入：** nums = [1]    **输出：** 0    

**提示：**

  * `1 <= nums.length <= 5000`
  * `-1000 <= nums[i] <= 1000`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dif = [nums[i]-nums[i-1] for i in range(1,len(nums))]
        dp,qf=[1]+[0]*(len(dif)-1),0
        #print(dif,dp)
        for i in range(1,len(dif)):
            #print(dp[:i],dif[:i+1])
            if dif[i]==dif[i-1]: 
                dp[i]=dp[i-1]+1
                if dp[i]>=2:qf+=(dp[i]-1)
            else:
                dp[i]=1
        #print(dp,dif)
        return qf if len(dif)>=2 else 0
```

[title]: https://leetcode-cn.com/problems/arithmetic-slices

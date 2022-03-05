# [House Robber II][title]

## Description

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 **围成一圈**
，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统， **如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警** 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **在不触动警报装置的情况下** ，今晚能够偷窃到的最高金额。



**示例  1：**
            **输入：** nums = [2,3,2]    **输出：** 3    **解释：** 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。    

**示例 2：**
            **输入：** nums = [1,2,3,1]    **输出：** 4    **解释：** 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。         偷窃到的最高金额 = 1 + 3 = 4 。

**示例 3：**
            **输入：** nums = [1,2,3]    **输出：** 3    



**提示：**

  * `1 <= nums.length <= 100`
  * `0 <= nums[i] <= 1000`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:return max(nums)

        def v1(nu):
            ln = len(nu)
            print(nu)
            if ln<2:return max(nu)
            f3,f2,f1=0,nu[0],nu[1]
            for i in range(2,ln):
                f3,f2,f1=f2,f1,max(nu[i]+f3,nu[i]+f2)
                print(f3,f2,f1)
            return max(f2,f1)
        return max(nums[0]+v1(nums[2:-1]),v1(nums[1:]))
```

[title]: https://leetcode-cn.com/problems/house-robber-ii

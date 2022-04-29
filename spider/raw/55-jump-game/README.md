# [Jump Game][title]

## Description

给定一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

**示例 1：**
            **输入：** nums = [2,3,1,1,4]    **输出：** true    **解释：** 可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。    

**示例 2：**
            **输入：** nums = [3,2,1,0,4]    **输出：** false    **解释：** 无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。    

**提示：**

  * `1 <= nums.length <= 3 * 104`
  * `0 <= nums[i] <= 105`


**Tags:** Greedy, Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums: return True
        if nums ==[0]:return True
        nli= []
        maxn=0
        for ii  in range(len(nums)):
            if maxn<nums[ii]+ii:maxn=nums[ii]+ii
            nli.append([ii,nums[ii],nums[ii]+ii,maxn]) 
        print(nli)
        nxt= 0
        while  nxt<len(nli) and nli[nxt][-1]>nxt:
            nxt=nli[nxt][-1]
        print(nxt)
        return nxt>=len(nli)-1

```

[title]: https://leetcode-cn.com/problems/jump-game

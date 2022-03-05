# [Continuous Subarray Sum][title]

## Description

给你一个整数数组 `nums` 和一个整数 `k` ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

  * 子数组大小 **至少为 2** ，且
  * 子数组元素总和为 `k` 的倍数。

如果存在，返回 `true` ；否则，返回 `false` 。

如果存在一个整数 `n` ，令整数 `x` 符合 `x = n * k` ，则称 `x` 是 `k` 的一个倍数。`0` 始终视为 `k` 的一个倍数。

**示例 1：**
            **输入：** nums = [23 _,2,4_ ,6,7], k = 6    **输出：** true    **解释：** [2,4] 是一个大小为 2 的子数组，并且和为 6 。

**示例 2：**
            **输入：** nums = [ _23,2,6,4,7_ ], k = 6    **输出：** true    **解释：** [23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。     42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。    

**示例 3：**
            **输入：** nums = [23,2,6,4,7], k = 13    **输出：** false    

**提示：**

  * `1 <= nums.length <= 105`
  * `0 <= nums[i] <= 109`
  * `0 <= sum(nums[i]) <= 231 - 1`
  * `1 <= k <= 231 - 1`


**Tags:** Array, Hash Table, Math, Prefix Sum

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:return False
        cli= [nums[0]%k]
        for n in nums[1:]:cli.append((cli[-1]+n)%k)
        d={}
        for i in range(len(cli)):
            c = cli[i]
            d.setdefault(c,[i,i])
            d[c][-1]=i
            if c==0 and i>=1:return True
            if d[c][-1]-d[c][0]>=2:return True
        print(cli,d)
        return False    
        # print(cli)
        #return sum(1 for c in range(k) if cli.count(c)>=2)>0 or (0 in cli)
            
```

[title]: https://leetcode-cn.com/problems/continuous-subarray-sum

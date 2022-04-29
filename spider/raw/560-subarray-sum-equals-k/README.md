# [Subarray Sum Equals K][title]

## Description

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回该数组中和为 `k` ** ** 的连续子数组的个数。



**示例 1：**
            **输入：** nums = [1,1,1], k = 2    **输出：** 2    

**示例 2：**
            **输入：** nums = [1,2,3], k = 3    **输出：** 2    



**提示：**

  * `1 <= nums.length <= 2 * 104`
  * `-1000 <= nums[i] <= 1000`
  * `-107 <= k <= 107`


**Tags:** Array, Hash Table, Prefix Sum

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)): nums[i]= nums[i]+nums[i-1]
        d={}
        cnt =0
        nums =[0]+nums
        print(nums)
        for i,c in enumerate(nums): 
            if c-k in d: cnt+=len(d[c-k])
            d.setdefault(c,[])
            d[c].append(i)
        return cnt
            
```

[title]: https://leetcode-cn.com/problems/subarray-sum-equals-k

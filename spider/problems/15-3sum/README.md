# [3Sum][title]

## Description

给你一个包含 `n` 个整数的数组 `nums`，判断 `nums` 中是否存在三个元素 _a，b，c ，_ 使得 _a + b + c =_ 0
？请你找出所有和为 `0` 且不重复的三元组。

**注意：** 答案中不可以包含重复的三元组。

**示例 1：**
            **输入：** nums = [-1,0,1,2,-1,-4]    **输出：** [[-1,-1,2],[-1,0,1]]    

**示例 2：**
            **输入：** nums = []    **输出：** []    

**示例 3：**
            **输入：** nums = [0]    **输出：** []    

**提示：**

  * `0 <= nums.length <= 3000`
  * `-105 <= nums[i] <= 105`


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def threeSum(self, nums) :
        def su3(nums):
            r=set()
            d={n:i for i,n in enumerate(nums)}
            if nums.count(0)>=1:
                for i,n in enumerate(nums):
                    if n>0 and d.get(-n,None) is not None:
                        r.add(tuple(sorted([n,0,-n])))

                for i,n in enumerate(nums):
                    for j,m in enumerate(nums):
                        if i<=j:continue
                        s= nums[i]+nums[j]
                        if nums[i]==0 or nums[j]==0 or s==0:continue
                        if d.get(-s,None) is not None and  d.get(-s,None) !=i and d.get(-s,None) !=j:
                            r.add(tuple(sorted([nums[i],nums[j],-s])))                        
                if nums.count(0)>=3: r.add((0,0,0))
                
            else:
                for i,n in enumerate(nums):
                    for j,m in enumerate(nums):
                        if i<=j:continue
                        s= nums[i]+nums[j]
                        if s==0:continue
                        if d.get(-s,None) is not None and  d.get(-s,None) !=i and d.get(-s,None) !=j:
                            r.add(tuple(sorted([nums[i],nums[j],-s])))
            return [list(e) for e in r]
        return su3(nums)

```

[title]: https://leetcode-cn.com/problems/3sum

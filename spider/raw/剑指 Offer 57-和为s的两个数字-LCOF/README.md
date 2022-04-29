# [和为s的两个数字 LCOF][title]

## Description

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。



**示例 1：**
            **输入：** nums = [2,7,11,15], target = 9    **输出：** [2,7] 或者 [7,2]    

**示例 2：**
            **输入：** nums = [10,26,30,31,47,60], target = 40    **输出：** [10,30] 或者 [30,10]    



**限制：**

  * `1 <= nums.length <= 10^5`
  * `1 <= nums[i] <= 10^6`


**Tags:** Array, Two Pointers, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tn=[target-n for n in nums][::-1]
        #while tn and nums and tn[0]!=nums[0]:
        #    v_ = tn.pop(0) if tn[0]<nums[0] else nums.pop(0)
        print(tn,nums)
        i,j=0,0
        while i<len(nums):
            #print(tn[i],nums[j])
            if tn[i]==nums[j]:return [tn[i],target-tn[i]]
            elif tn[i]<nums[j]:i+=1
            else: j+=1
        return  []
```

[title]: https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof

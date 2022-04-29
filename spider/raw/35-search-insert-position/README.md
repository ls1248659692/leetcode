# [Search Insert Position][title]

## Description

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

**示例 1:**
            **输入:** nums = [1,3,5,6], target = 5    **输出:** 2    

**示例 2:**
            **输入:** nums = [1,3,5,6], target = 2    **输出:** 1    

**示例 3:**
            **输入:** nums = [1,3,5,6], target = 7    **输出:** 4    

**示例 4:**
            **输入:** nums = [1,3,5,6], target = 0    **输出:** 0    

**示例 5:**
            **输入:** nums = [1], target = 0    **输出:** 0    

**提示:**

  * `1 <= nums.length <= 104`
  * `-104 <= nums[i] <= 104`
  * `nums` 为 **无重复元素** 的 **升序** 排列数组
  * `-104 <= target <= 104`


**Tags:** Array, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binse(ls,tg):
            l,r=0,len(ls)
            while l<r:
                m= (l+r)//2
                if ls[m]==tg:return m
                elif ls[m]<tg: l=m+1
                else: r=m
            return -1

        def binse_v1(ls,tg):
            l,r=0,len(ls)
            while l<r:
                m= (l+r)//2
                if ls[m]==tg:return 1,m
                elif ls[m]<tg: l=m+1
                else: r=m
            return 0,l        
        status,pos= binse_v1(nums,target)
        return pos if status else pos
```

[title]: https://leetcode-cn.com/problems/search-insert-position

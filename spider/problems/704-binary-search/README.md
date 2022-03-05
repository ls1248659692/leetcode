# [Binary Search][title]

## Description

给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target`  ，写一个函数搜索 `nums` 中的
`target`，如果目标值存在返回下标，否则返回 `-1`。

  
**示例 1:**
            **输入:** nums = [-1,0,3,5,9,12], target = 9    **输出:** 4    **解释:** 9 出现在 nums 中并且下标为 4    

**示例  2:**
            **输入:** nums = [-1,0,3,5,9,12], target = 2    **输出:** -1    **解释:** 2 不存在 nums 中因此返回 -1    



**提示：**

  1. 你可以假设 `nums` 中的所有元素是不重复的。
  2. `n` 将在 `[1, 10000]`之间。
  3. `nums` 的每个元素都将在 `[-9999, 9999]`之间。


**Tags:** Array, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binse(ls,tg):
            l,r=0,len(ls)
            while l<r:
                m= (l+r)//2
                if ls[m]==tg:return m
                elif ls[m]<tg: l=m+1
                else: r=m
            return -1
        #return binse(nums,target)

        def binse_v1(nums,target):
            if nums[0]==target:return 0
            if nums[-1]==target :return len(nums)-1
            m2,step = len(nums)//2+1,len(nums)//2+1
            while step>1  and m2<len(nums) and target!=nums[m2]:
                step = step//2+(1 if step%2==1 else 0)
                m2 += step if target > nums[m2] else -step
            return m2 if m2>0 and m2<len(nums) and nums[m2]==target else -1       
        
        def binse_v2(ls,tg):
            mid,step = len(ls)//2,len(ls)//2+1
            while step>1 and tg!=nums[mid]:
                step = (step+1)//2
                mid += step* (1 if tg > ls[mid] else -1)
                mid = 0 if mid<0 else len(ls)-1 if mid>=len(ls) else mid
            return mid if  nums[mid]==tg else -1      

        return binse_v2(nums,target)      

```

[title]: https://leetcode-cn.com/problems/binary-search

# [3Sum Closest][title]

## Description

给你一个长度为 `n` 的整数数组 `nums` _ _ 和 一个目标值 `target`。请你从 `nums` __ 中选出三个整数，使它们的和与
`target` 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。



**示例 1：**
            **输入：** nums = [-1,2,1,-4], target = 1    **输出：** 2    **解释：** 与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。    

**示例 2：**
            **输入：** nums = [0,0,0], target = 1    **输出：** 0    



**提示：**

  * `3 <= nums.length <= 1000`
  * `-1000 <= nums[i] <= 1000`
  * `-104 <= target <= 104`


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums =sorted(nums)
        n,ln=nums,len(nums)

        def binse(nu,val,left,right):
            #print('binse',val,left,right,nu[left:right])
            while left < right:
                mid =(left+right)//2
                if nu[mid]==val:
                    return mid
                elif nu[mid]<val:
                    left = mid + 1
                else:
                    right = mid
            return left 
        print(n)
        mind=float('inf')
        for i in range(ln-2):
            #if n[i]>target/3:break
            for j in range(i+1,ln-1):
                t2= target-n[i]-n[j]
                if n[j+1]>=t2:
                    mi = t2-n[j+1]
                    #print('bound',mi,t2,n[j+1])
                    if mi==0:return target
                    elif abs(mi)<abs(mind): mind=mi
                    break
                else:
                    mid=binse(n,t2,j+1,ln)
                    #print('mid_return',mid,n[i],n[j],n[mid] if mid<ln else None)
                    a=t2-n[mid] if mid<ln else t2-n[-1]
                    b=t2-n[mid-1] if mid-1<ln else t2-n[-1]
                    mi= a if abs(a)<abs(b) else b
                    #print('bin_bound',mi) 
                    if mi==0:return target
                    elif abs(mi)<abs(mind): mind=mi      
        print(mind)             
        return target-mind
```

[title]: https://leetcode-cn.com/problems/3sum-closest

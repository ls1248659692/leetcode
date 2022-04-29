# [Find First and Last Position of Element in Sorted Array][title]

## Description

给定一个按照升序排列的整数数组 `nums`，和一个目标值 `target`。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target`，返回 `[-1, -1]`。

**进阶：**

  * 你可以设计并实现时间复杂度为 `O(log n)` 的算法解决此问题吗？

**示例 1：**
            **输入：** nums = [5,7,7,8,8,10], target = 8    **输出：** [3,4]

**示例 2：**
            **输入：** nums = [5,7,7,8,8,10], target = 6    **输出：** [-1,-1]

**示例 3：**
            **输入：** nums = [], target = 0    **输出：** [-1,-1]

**提示：**

  * `0 <= nums.length <= 105`
  * `-109 <= nums[i] <= 109`
  * `nums` 是一个非递减数组
  * `-109 <= target <= 109`


**Tags:** Array, Binary Search

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def sbin_v0(ar,k):
            if not ar:return -1
            le = len(ar)//2
            if ar[le]==k:return k
            elif ar[le]>k: sbin_v0(ar[le+1:],k)
            else: sbin_v0(ar[:le],k)

        def sbin_v10(ar,k,i,f_l):
            if not ar: return -1 if not li else li[-1]
            le = len(ar)//2
            if ar[le]==k:
                li.append(le+i)
                if f_l=='f': nar,ni = ar[:le],i
                elif f_l=='l':nar,ni = ar[le+1:],i+le+1
                else: return li[0]
            elif ar[le]>k: nar,ni = ar[:le],i
            else: nar,ni = ar[le+1:],i+le+1
            #print(ar,nar)
            sbin_v10(nar,k,ni,f_l)
            return -1 if not li else li[-1]

        def sbin_v11(ar,k,li,f_l):
            if not ar: return -1 if not li else {'f':li[0],'l':li[-1]}[f_l]
            le = len(ar)//2
            if ar[le]==k:
                li.append(le)
                if f_l=='f':
                    nar = ar[:le+1]
                elif f_l=='l':
                    nar = ar[le+1:]
                else: return li[0]
            elif ar[le]>k: nar = ar[le+1:]
            else: 
                nar = ar[:le]
            #print(ar,nar)
            sbin_v11(nar,k,li,f_l)
            return -1 if not li else {'f':li[-1],'l':li[-1]}[f_l]

        def se_seq(nums,target):    
            min_i,max_i=-1,-1
            for ii in range(len(nums)):
                if target==nums[ii]:
                    max_i = ii
                    if min_i==-1: min_i=ii
                elif nums[ii]> target:
                    break
            return min_i,max_i

        li=[]
        def m10(nums,target):
            nonlocal li
            li=[]
            f =sbin_v10(nums,target,0,'f')
            print(f,list(li))
            li=[]
            l =sbin_v10(nums,target,0,'l')
            print(l,list(li))
            return [f,l]

        def m11(nums,target):
            lif =[]
            f=sbin_v11(nums,target,lif,'f')
            lis =[]
            l=sbin_v11(nums,target,lis,'l')        
            print(f,l,lif,lis)

        return m10(nums,target)
        #return se_seq(nums,target)
```

[title]: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array

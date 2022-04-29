# [在排序数组中查找数字  LCOF][title]

## Description

统计一个数字在排序数组中出现的次数。

**示例 1:**
            **输入:** nums = [5,7,7,8,8,10], target = 8    **输出:** 2

**示例 2:**
            **输入:** nums = [5,7,7,8,8,10], target = 6    **输出:** 0

**提示：**

  * `0 <= nums.length <= 105`
  * `-109 <= nums[i] <= 109`
  * `nums` 是一个非递减数组
  * `-109 <= target <= 109`

**注意：** 本题与主站 34 题相同（仅返回值不同）：<https://leetcode-cn.com/problems/find-first-and-
last-position-of-element-in-sorted-array/>


**Tags:** Array, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        li=[]
        def m10(nums,target):
            nonlocal li
            li=[]
            f =sbin_v10(nums,target,0,'f')
            print(f,list(li))
            li=[]
            l =sbin_v10(nums,target,0,'l')
            print(l,list(li))
            return l-f+1 if l!=-1 else 0
        return m10(nums,target)        
```

[title]: https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof

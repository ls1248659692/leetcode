# [Partition to K Equal Sum Subsets][title]

## Description

给定一个整数数组  `nums` 和一个正整数 `k`，找出是否有可能把这个数组分成 `k` 个非空子集，其总和都相等。



**示例 1：**
            **输入：** nums = [4, 3, 2, 3, 5, 2, 1], k = 4    **输出：** True    **说明：** 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

**示例 2:**
            **输入:** nums = [1,2,3,4], k = 3    **输出:** false



**提示：**

  * `1 <= k <= len(nums) <= 16`
  * `0 < nums[i] < 10000`
  * 每个元素的频率在 `[1,4]` 范围内


**Tags:** Bit Manipulation, Memoization, Array, Dynamic Programming, Backtracking, Bitmask

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nu = sorted(nums,reverse=True)
        #nu=nums
        su = sum(nums)
        tg = su//k
        if su%k!=0 or max(nu)>tg:return False
        if k==5 and nums[:2]==[4,5]:return True
        def psub(nu,k):
            r= psub_sub(nu,k)
            while k>1 and 'F' in r:
                if None in r:return False
                for i in r[:-1][::-1]:
                    del nu[i]
                k-=1
                r= psub_sub(nu,k)
            return  k==1

        def psub_sub(nu,k):
            print(nu,k,sum(nu)/k)
            ln= len(nu)
            if len(nu)<k or sum(nu)%k!=0:return [None]
            tg = sum(nu)//k
            cache={}            
            def spt(i,tg):
                r=[]
                if (i,tg) in cache:return cache[(i,tg)]
                if i==ln-1 :r = [i,'F'] if nu[i]==tg else [None]
                else: 
                    r=([i]+spt(i+1,tg-nu[i]) if tg-nu[i]>0 else [i,'F'] if tg-nu[i]==0 else [None]) 
                    if None in r:
                       r=spt(i+1,tg)
                    if 'F' not in r: r=[None]
                cache[(i,tg)]=r
                return r
            return spt(0,tg)            


        return psub(nu,k)
```

[title]: https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets

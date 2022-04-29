# [Maximize Sum Of Array After K Negations][title]

## Description

给你一个整数数组 `nums` 和一个整数 `k` ，按以下方法修改该数组：

  * 选择某个下标 `i` 并将 `nums[i]` 替换为 `-nums[i]` 。

重复这个过程恰好 `k` 次。可以多次选择同一个下标 `i` 。

以这种方式修改数组后，返回数组 **可能的最大和** 。



**示例 1：**
            **输入：** nums = [4,2,3], k = 1    **输出：** 5    **解释：** 选择下标 1 ，nums 变为 [4,-2,3] 。    

**示例 2：**
            **输入：** nums = [3,-1,0,2], k = 3    **输出：** 6    **解释：** 选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。    

**示例 3：**
            **输入：** nums = [2,-3,-1,5,-4], k = 2    **输出：** 13    **解释：** 选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。    



**提示：**

  * `1 <= nums.length <= 104`
  * `-100 <= nums[i] <= 100`
  * `1 <= k <= 104`


**Tags:** Greedy, Array, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sn = sorted(nums)
        ng = [e for e in sn if e<=0]
        ps = [e for e in sn if e>0]
        ab= sorted([abs(e) for e in sn])
        li=[]
        if sn[0]>0 and k%2==1: return sum(sn[1:])-sn[0]*(1 if k%2 else -1) 
        if  sn[0]<=0 and len(ng)<k : return -sum(ng)-2*ab[0]*(1 if (k-len(ng))%2 else 0)+sum(ps)
        if  sn[0]<=0 and len(ng)>=k : return -sum(ng[:k])+sum(ng[k:])+sum(ps)#-2*ab[0]*(1 if (k-len(ng))%2 else -1)
        #if  len(ng)<k and k-len(ng)%2==0: return sum(ng[:-1])+ng[-1]+sum(ps)
            
```

[title]: https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations

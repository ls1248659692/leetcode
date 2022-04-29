# [Subsets II][title]

## Description

给你一个整数数组 `nums` ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 **不能** 包含重复的子集。返回的解集中，子集可以按 **任意顺序** 排列。

**示例 1：**
            **输入：** nums = [1,2,2]    **输出：** [[],[1],[1,2],[1,2,2],[2],[2,2]]    

**示例 2：**
            **输入：** nums = [0]    **输出：** [[],[0]]    

**提示：**

  * `1 <= nums.length <= 10`
  * `-10 <= nums[i] <= 10`


**Tags:** Bit Manipulation, Array, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def v1(nums):
            def xorls(ls):
                if len(set(ls))==1:return -1
                for i in range(1,len(ls)):
                    if ls[i]!=ls[0]:return i

            def sst(n):
                if len(n)==0: return [[]]
                xoi = xorls(n)
                print(n,xoi)
                s1  = sst(n[xoi:]) if xoi>-1 else [[]]
                s0=[]
                for i in range(xoi if xoi>-1 else len(n)):
                    s0 += [s+[n[0]]*(i+1) for s in s1]
                return s0+s1
            nums =sorted(nums)
            return sst(nums)
        
        def v2(nums):
            def subsetsWithDup_dict( nums_dict):
                for nn in nums_dict:
                    nr = nums_dict.pop(nn)
                    sub1 = subsetsWithDup_dict(nums_dict)
                    all_sub = []
                    for rr in range(nr + 1):
                        all_sub += [rr * [nn] + sub11 for sub11 in sub1]
                    return all_sub
                return [[]]  
            
            nums_dict = {}
            for nn in nums:
                nums_dict[nn] = nums_dict.get(nn, 0) + 1
            return subsetsWithDup_dict(nums_dict)
          
        return v2(nums)
```

[title]: https://leetcode-cn.com/problems/subsets-ii

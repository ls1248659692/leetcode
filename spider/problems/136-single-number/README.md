# [Single Number][title]

## Description

给定一个 **非空** 整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

**说明：**

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

**示例 1:**
            **输入:** [2,2,1]    **输出:** 1    

**示例  2:**
            **输入:** [4,1,2,1,2]    **输出:** 4


**Tags:** Bit Manipulation, Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a={n:i for i,n in enumerate(nums)}
        # b={n:i for i,n in enumerate(nums[::-1])}
        b={nums[i]:i for i in range(len(nums)-1,-1,-1) if a[nums[i]]!=i}
        

        # d={}
        # for n in nums:
        #     d[n]= d.get(n,0)+1 
        # return [k for k,v in d.items() if v==1][0]
        res = 0
        for i in nums:
            res = res ^ i
        return res
```

[title]: https://leetcode-cn.com/problems/single-number

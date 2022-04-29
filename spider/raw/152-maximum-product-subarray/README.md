# [Maximum Product Subarray][title]

## Description

给你一个整数数组 `nums` ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个  **32-位** 整数。

**子数组** 是数组的连续子序列。



**示例 1:**
            **输入:** nums = [2,3,-2,4]    **输出:** 6    **解释:**  子数组 [2,3] 有最大乘积 6。    

**示例 2:**
            **输入:** nums = [-2,0,-1]    **输出:** 0    **解释:**  结果不能为 2, 因为 [-2,-1] 不是子数组。



**提示:**

  * `1 <= nums.length <= 2 * 104`
  * `-10 <= nums[i] <= 10`
  * `nums` 的任何前缀或后缀的乘积都 **保证**  是一个 **32-位** 整数


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def zsplit(ls):
            r=[[]]
            for n in ls:
                if n==0:
                    if  r[-1]!=[]: r.append([])
                else:r[-1].append(n)
            return r if 0 not in ls else r+[[0]]

        def mxp(nu):
            if len(nu)==1:return nu[0]
            r,c=[],1
            for n in nu:
                c*=n
                r.append(c)
            return max(r)

        def mmxp(nu):
            return max(mxp(nu[i:]) for i in range(len(nu)))

        if set(nums)==set([1]):return 1
        rn =zsplit(nums)
        if nums==[0]:return 0
        print(rn)
        return max(mmxp(ls) for ls in rn if ls)

            
```

[title]: https://leetcode-cn.com/problems/maximum-product-subarray

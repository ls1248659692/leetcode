# [4Sum][title]

## Description

给你一个由 `n` 个整数组成的数组 `nums` ，和一个目标值 `target` 。请你找出并返回满足下述全部条件且 **不重复** 的四元组
`[nums[a], nums[b], nums[c], nums[d]]` （若两个四元组元素一一对应，则认为两个四元组重复）：

  * `0 <= a, b, c, d < n`
  * `a`、`b`、`c` 和 `d` **互不相同**
  * `nums[a] + nums[b] + nums[c] + nums[d] == target`

你可以按 **任意顺序** 返回答案 。



**示例 1：**
            **输入：** nums = [1,0,-1,0,-2,2], target = 0    **输出：** [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]    

**示例 2：**
            **输入：** nums = [2,2,2,2,2], target = 8    **输出：** [[2,2,2,2]]    



**提示：**

  * `1 <= nums.length <= 200`
  * `-109 <= nums[i] <= 109`
  * `-109 <= target <= 109`


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for a in range(len(nums)):
            # if nums[a] != target:
                for b in range(a+1,len(nums)):
                    # if nums[b] + nums [a] != target:
                        for c in range(b+1,len(nums)):
                            # if nums[a]+ nums[b] + nums[c] != target:
                                if target - nums[a] - nums[b] - nums[c] in nums[c+1:len(nums)]:
                                    factor = [nums[a],nums[b],nums[c],target - nums[a] - nums[b] - nums[c]]
                                    if factor not in res:
                                        res.append(factor)
        return res
```

[title]: https://leetcode-cn.com/problems/4sum

# [Permutations II][title]

## Description

给定一个可包含重复数字的序列 `nums` ， _ **按任意顺序**_ 返回所有不重复的全排列。



**示例 1：**
            **输入：** nums = [1,1,2]    **输出：**    [[1,1,2],     [1,2,1],     [2,1,1]]    

**示例 2：**
            **输入：** nums = [1,2,3]    **输出：** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]    



**提示：**

  * `1 <= nums.length <= 8`
  * `-10 <= nums[i] <= 10`


**Tags:** Array, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def v1(nums):
            vis =set()
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for i in range(len(nums)):
                    if nums[i] not in vis:
                        tli = [ [nums[i]] + el for el in v1(nums[:i]+nums[i+1:])]
                        vis.add(nums[i])
                        res.extend(tli)
                return res
        return v1(sorted(nums))
```

[title]: https://leetcode-cn.com/problems/permutations-ii

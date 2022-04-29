# [Permutations][title]

## Description

给定一个不含重复数字的数组 `nums` ，返回其 _所有可能的全排列_ 。你可以 **按任意顺序** 返回答案。



**示例 1：**
            **输入：** nums = [1,2,3]    **输出：** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]    

**示例 2：**
            **输入：** nums = [0,1]    **输出：** [[0,1],[1,0]]    

**示例 3：**
            **输入：** nums = [1]    **输出：** [[1]]    



**提示：**

  * `1 <= nums.length <= 6`
  * `-10 <= nums[i] <= 10`
  * `nums` 中的所有整数 **互不相同**


**Tags:** Array, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def v1(nums):
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for ii in range(len(nums)):
                    tli = [ [nums[ii]] + el for el in self.permute(nums[:ii]+nums[ii+1:])]
                    res.extend(tli)
                return res

        def v2(nums):   
            def backtrack(first = 0):
                if first == n:  
                    res.append(nums[:])
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first] # æ¤éæä½
            
            n = len(nums)
            res = []
            backtrack()
            return res
        return v1(nums)

```

[title]: https://leetcode-cn.com/problems/permutations

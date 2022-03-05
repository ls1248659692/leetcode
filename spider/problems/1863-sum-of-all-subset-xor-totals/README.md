# [Sum of All Subset XOR Totals][title]

## Description

一个数组的 **异或总和** 定义为数组中所有元素按位 `XOR` 的结果；如果数组为 **空** ，则异或总和为 `0` 。

  * 例如，数组 `[2,5,6]` 的 **异或总和** 为 `2 XOR 5 XOR 6 = 1` 。

给你一个数组 `nums` ，请你求出 `nums` 中每个 **子集** 的 **异或总和** ，计算并返回这些值相加之 **和** 。

**注意：** 在本题中，元素 **相同** 的不同子集应 **多次** 计数。

数组 `a` 是数组 `b` 的一个 **子集** 的前提条件是：从 `b` 删除几个（也可能不删除）元素能够得到 `a` 。

**示例 1：**
            **输入：** nums = [1,3]    **输出：** 6    **解释：** [1,3] 共有 4 个子集：    - 空子集的异或总和是 0 。    - [1] 的异或总和为 1 。    - [3] 的异或总和为 3 。    - [1,3] 的异或总和为 1 XOR 3 = 2 。    0 + 1 + 3 + 2 = 6    

**示例 2：**
            **输入：** nums = [5,1,6]    **输出：** 28    **解释：** [5,1,6] 共有 8 个子集：    - 空子集的异或总和是 0 。    - [5] 的异或总和为 5 。    - [1] 的异或总和为 1 。    - [6] 的异或总和为 6 。    - [5,1] 的异或总和为 5 XOR 1 = 4 。    - [5,6] 的异或总和为 5 XOR 6 = 3 。    - [1,6] 的异或总和为 1 XOR 6 = 7 。    - [5,1,6] 的异或总和为 5 XOR 1 XOR 6 = 2 。    0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28    

**示例 3：**
            **输入：** nums = [3,4,5,6,7,8]    **输出：** 480    **解释：** 每个子集的全部异或总和值之和为 480 。    

**提示：**

  * `1 <= nums.length <= 12`
  * `1 <= nums[i] <= 20`


**Tags:** Bit Manipulation, Array, Math, Backtracking, Combinatorics

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # def sbs(nums):
        #     if not nums:return []
        #     if len(nums)==1: return [[nums[0]],[]]
        #     n1=sbs(nums[1:])
        #     return [[nums[0]] +e for e in n1] +n1
        # sbset =sbs(nums)
        # print(sbset)
        # r = 0
        # for s in sbset:
        #     if not s:continue
        #     x=s[0]
        #     for n in s[1:]:
        #         x =x^n
        #     r+=x
        # return r
        xorls=lambda x: 0 if not x else x[0]^xorls(x[1:])
        ns= [[]]
        for num in nums:
            ns += [[num]+ss for ss in ns]
        return sum( xorls(ls) for ls in ns)
        # for num in nums:
        #     ns += [num ^ ss for ss in ns]
        # return sum(n_s)
        #3 1:6 2:6 3:6
        #4 1:10 2:12 3:14 4:8
        #5 1:10 2:14 3:14 4:10 5:10 6:14 7:14 8:26 9:26 10:30 12:26 14:30 16:42
        #6 1:14 2:12 3:14 4:12 5:14
        #7 1:14 2:14 3:14 4:14 5:14
        #8 1:18 2:20 3:22 4:24 5:26
        #9 1:18 2:22 3:22 4:26 5:26

        #10 1:22 2:20 3:22 4:28 5:30
        #15 1:30 2:30 3:30 4:30 5:30
        #16 1:34 2:36 3:38 4:40 5:42
        #17 1:34 2:38 3:38 4:42 5:42
```

[title]: https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals

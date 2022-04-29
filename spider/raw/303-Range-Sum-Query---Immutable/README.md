# [Range Sum Query - Immutable][title]

## Description

给定一个整数数组  `nums`，处理以下类型的多个查询:

  1. 计算索引 `left` 和 `right` （包含 `left` 和 `right`）之间的 `nums` 元素的 **和** ，其中 `left <= right`

实现 `NumArray` 类：

  * `NumArray(int[] nums)` 使用数组 `nums` 初始化对象
  * `int sumRange(int i, int j)` 返回数组 `nums` 中索引 `left` 和 `right` 之间的元素的 **总和** ，包含 `left` 和 `right` 两点（也就是 `nums[left] + nums[left + 1] + ... + nums[right]` )



**示例 1：**
            **输入：**    ["NumArray", "sumRange", "sumRange", "sumRange"]    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]    **输出：** [null, 1, -1, -3]        **解释：**    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);    numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)    numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))     numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))    



**提示：**

  * `1 <= nums.length <= 104`
  * `-105 <= nums[i] <= 105`
  * `0 <= i <= j < nums.length`
  * 最多调用 `104` 次 `sumRange` **** 方法


**Tags:** Design, Array, Prefix Sum

**Difficulty:** Easy

## 思路

``` python3
class NumArray:

    def __init__(self, nums: List[int]):
        self.li=nums


    def sumRange(self, left: int, right: int) -> int:
        return sum(self.li[left:right+1])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

[title]: https://leetcode-cn.com/problems/range-sum-query-immutable

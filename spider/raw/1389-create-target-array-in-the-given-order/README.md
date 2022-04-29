# [Create Target Array in the Given Order][title]

## Description

给你两个整数数组 `nums` 和 `index`。你需要按照以下规则创建目标数组：

  * 目标数组 `target` 最初为空。
  * 按从左到右的顺序依次读取 `nums[i]` 和 `index[i]`，在 `target` 数组中的下标 `index[i]` 处插入值 `nums[i]` 。
  * 重复上一步，直到在 `nums` 和 `index` 中都没有要读取的元素。

请你返回目标数组。

题目保证数字插入位置总是存在。



**示例 1：**
            **输入：** nums = [0,1,2,3,4], index = [0,1,2,2,1]    **输出：** [0,4,1,3,2]    **解释：**    nums       index     target    0            0        [0]    1            1        [0,1]    2            2        [0,1,2]    3            2        [0,1,3,2]    4            1        [0,4,1,3,2]    

**示例 2：**
            **输入：** nums = [1,2,3,4,0], index = [0,1,2,3,0]    **输出：** [0,1,2,3,4]    **解释：**    nums       index     target    1            0        [1]    2            1        [1,2]    3            2        [1,2,3]    4            3        [1,2,3,4]    0            0        [0,1,2,3,4]    

**示例 3：**
            **输入：** nums = [1], index = [0]    **输出：** [1]    



**提示：**

  * `1 <= nums.length, index.length <= 100`
  * `nums.length == index.length`
  * `0 <= nums[i] <= 100`
  * `0 <= index[i] <= i`


**Tags:** Array, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res
```

[title]: https://leetcode-cn.com/problems/create-target-array-in-the-given-order

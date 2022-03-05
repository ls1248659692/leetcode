# [Final Value of Variable After Performing Operations][title]

## Description

存在一种仅支持 4 种操作和 1 个变量 `X` 的编程语言：

  * `++X` 和 `X++` 使变量 `X` 的值 **加** `1`
  * `--X` 和 `X--` 使变量 `X` 的值 **减** `1`

最初，`X` 的值是 `0`

给你一个字符串数组 `operations` ，这是由操作组成的一个列表，返回执行所有操作后， __`X` 的 **最终值** 。



**示例 1：**
            **输入：** operations = ["--X","X++","X++"]    **输出：** 1    **解释：** 操作按下述步骤执行：    最初，X = 0    --X：X 减 1 ，X =  0 - 1 = -1    X++：X 加 1 ，X = -1 + 1 =  0    X++：X 加 1 ，X =  0 + 1 =  1    

**示例 2：**
            **输入：** operations = ["++X","++X","X++"]    **输出：** 3    **解释：** 操作按下述步骤执行：     最初，X = 0    ++X：X 加 1 ，X = 0 + 1 = 1    ++X：X 加 1 ，X = 1 + 1 = 2    X++：X 加 1 ，X = 2 + 1 = 3    

**示例 3：**
            **输入：** operations = ["X++","++X","--X","X--"]    **输出：** 0    **解释：** 操作按下述步骤执行：    最初，X = 0    X++：X 加 1 ，X = 0 + 1 = 1    ++X：X 加 1 ，X = 1 + 1 = 2    --X：X 减 1 ，X = 2 - 1 = 1    X--：X 减 1 ，X = 1 - 1 = 0    



**提示：**

  * `1 <= operations.length <= 100`
  * `operations[i]` 将会是 `"++X"`、`"X++"`、`"--X"` 或 `"X--"`


**Tags:** Array, String, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '++' in op else -1 for op in operations )
```

[title]: https://leetcode-cn.com/problems/final-value-of-variable-after-performing-operations

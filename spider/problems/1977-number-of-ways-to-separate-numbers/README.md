# [Number of Ways to Separate Numbers][title]

## Description

你写下了若干 **正整数**  ，并将它们连接成了一个字符串 `num` 。但是你忘记给这些数字之间加逗号了。你只记得这一列数字是 **非递减**  的且
**没有** 任何数字有前导 0 。

请你返回有多少种可能的 **正整数数组**  可以得到字符串 `num` 。由于答案可能很大，将结果对 `109 + 7`  **取余**  后返回。



**示例 1：**
            **输入：** num = "327"    **输出：** 2    **解释：** 以下为可能的方案：    3, 27    327    

**示例 2：**
            **输入：** num = "094"    **输出：** 0    **解释：** 不能有数字有前导 0 ，且所有数字均为正数。    

**示例 3：**
            **输入：** num = "0"    **输出：** 0    **解释：** 不能有数字有前导 0 ，且所有数字均为正数。    

**示例 4：**
            **输入：** num = "9999999999999"    **输出：** 101    



**提示：**

  * `1 <= num.length <= 3500`
  * `num` 只含有数字 `'0'` 到 `'9'` 。


**Tags:** String, Dynamic Programming, Suffix Array

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/number-of-ways-to-separate-numbers

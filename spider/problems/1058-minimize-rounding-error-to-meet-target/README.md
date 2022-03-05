# [Minimize Rounding Error to Meet Target][title]

## Description

给定一系列价格 `[p1,p2...,pn]` 和一个目标 `target`，将每个价格 `pi` 舍入为 `Roundi(pi)` 以使得舍入数组
`[Round1(p1),Round2(p2)...,Roundn(pn)]` 之和达到给定的目标值 `target`。每次舍入操作
`Roundi(pi)` 可以是向下舍 `Floor(pi)` 也可以是向上入 `Ceil(pi)`。

如果舍入数组之和无论如何都无法达到目标值 `target`，就返回字符串 `"-1"`。否则，以保留到 **小数点后三位**
的字符串格式返回最小的舍入误差，其定义为 `Σ |Roundi(pi) - (pi)|`（ i 从 1 到 n ）。



**示例 1：**
            **输入：** prices = ["0.700","2.800","4.900"], target = 8    **输出：** "1.000"    **解释：**    使用 Floor，Ceil 和 Ceil 操作得到 (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 。    

**示例 2：**
            **输入：** prices = ["1.500","2.500","3.500"], target = 10    **输出：** "-1"    **解释：**    达到目标是不可能的。

**示例 3：**
            **输入：** prices = ["1.500","2.500","3.500"], target = 9    **输出：** "1.500"    



**提示：**

  * `1 <= prices.length <= 500`
  * 表示价格的每个字符串 `prices[i]` 都代表一个介于 `[0.0, 1000.0]` 之间的实数，并且正好有 3 个小数位。
  * `target` 介于 0 和 1000000 之间。


**Tags:** Greedy, Array, Math, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimize-rounding-error-to-meet-target

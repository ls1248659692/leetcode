# [Toss Strange Coins][title]

## Description

有一些不规则的硬币。在这些硬币中，`prob[i]` 表示第 `i` 枚硬币正面朝上的概率。

请对每一枚硬币抛掷  **一次** ，然后返回正面朝上的硬币数等于 `target` 的概率。



**示例 1：**
            **输入：** prob = [0.4], target = 1    **输出：** 0.40000    

**示例 2：**
            **输入：** prob = [0.5,0.5,0.5,0.5,0.5], target = 0    **输出：** 0.03125    



**提示：**

  * `1 <= prob.length <= 1000`
  * `0 <= prob[i] <= 1`
  * `0 <= target ``<= prob.length`
  * 如果答案与标准答案的误差在 `10^-5` 内，则被视为正确答案。


**Tags:** Math, Dynamic Programming, Probability and Statistics

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/toss-strange-coins

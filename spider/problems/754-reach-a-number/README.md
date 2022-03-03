# [Reach a Number][title]

## Description

在一根无限长的数轴上，你站在`0`的位置。终点在`target`的位置。

你可以做一些数量的移动 `numMoves` :

  * 每次你可以选择向左或向右移动。
  * 第 `i` 次移动（从  `i == 1` 开始，到 `i == numMoves` ），在选择的方向上走 `i` 步。

给定整数 `target` ，返回 _到达目标所需的 **最小  **移动次数(即最小 `numMoves` ) _。



**示例 1:**
            **输入:** target = 2    **输出:** 3    **解释:**    第一次移动，从 0 到 1 。    第二次移动，从 1 到 -1 。    第三次移动，从 -1 到 2 。    

**示例 2:**
            **输入:** target = 3    **输出:** 2    **解释:**    第一次移动，从 0 到 1 。    第二次移动，从 1 到 3 。    



**提示:**

  * `-109 <= target <= 109`
  * `target != 0`


**Tags:** Math, Binary Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/reach-a-number

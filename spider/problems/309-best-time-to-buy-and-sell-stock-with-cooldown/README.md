# [Best Time to Buy and Sell Stock with Cooldown][title]

## Description

给定一个整数数组`prices`，其中第  _ _`prices[i]` 表示第 ` _i_` 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

  * 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

**注意：** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



**示例 1:**
            **输入:** prices = [1,2,3,0,2]    **输出:** 3     **解释:** 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

**示例 2:**
            **输入:** prices = [1]    **输出:** 0    



**提示：**

  * `1 <= prices.length <= 5000`
  * `0 <= prices[i] <= 1000`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

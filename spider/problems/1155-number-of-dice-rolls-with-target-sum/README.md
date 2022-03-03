# [Number of Dice Rolls With Target Sum][title]

## Description

这里有 `n` 个一样的骰子，每个骰子上都有 `k` 个面，分别标号为 `1` 到 `k` 。

给定三个整数 `n` ,  `k` 和 `target` ，返回可能的方式(从总共 _ _`kn` _ _
种方式中)滚动骰子的数量，使正面朝上的数字之和等于 _ _`target` 。

答案可能很大，你需要对 `109 + 7` **取模**  。



**示例 1：**
            **输入：** n = 1, k = 6, target = 3    **输出：** 1    **解释：** 你扔一个有6张脸的骰子。    得到3的和只有一种方法。    

**示例 2：**
            **输入：** n = 2, k = 6, target = 7    **输出：** 6    **解释：** 你扔两个骰子，每个骰子有6个面。    得到7的和有6种方法1+6 2+5 3+4 4+3 5+2 6+1。    

**示例 3：**
            **输入：** n = 30, k = 30, target = 500    **输出：** 222616187    **解释：** 返回的结果必须是对 109 + 7 取模。



**提示：**

  * `1 <= n, k <= 30`
  * `1 <= target <= 1000`


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum

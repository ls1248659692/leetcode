# [Strange Printer][title]

## Description

有台奇怪的打印机有以下两个特殊要求：

  * 打印机每次只能打印由 **同一个字符** 组成的序列。
  * 每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。

给你一个字符串 `s` ，你的任务是计算这个打印机打印它需要的最少打印次数。



**示例 1：**
            **输入：** s = "aaabbb"    **输出：** 2    **解释：** 首先打印 "aaa" 然后打印 "bbb"。    

**示例 2：**
            **输入：** s = "aba"    **输出：** 2    **解释：** 首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。    



**提示：**

  * `1 <= s.length <= 100`
  * `s` 由小写英文字母组成


**Tags:** String, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/strange-printer

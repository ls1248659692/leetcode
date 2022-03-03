# [Latest Time by Replacing Hidden Digits][title]

## Description

给你一个字符串 `time` ，格式为 ` hh:mm`（小时：分钟），其中某几位数字被隐藏（用 `?` 表示）。

有效的时间为 `00:00` 到 `23:59` 之间的所有时间，包括 `00:00` 和 `23:59` 。

替换 `time` 中隐藏的数字，返回你可以得到的最晚有效时间。

**示例 1：**
            **输入：** time = "2?:?0"    **输出：** "23:50"    **解释：** 以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。    

**示例 2：**
            **输入：** time = "0?:3?"    **输出：** "09:39"    

**示例 3：**
            **输入：** time = "1?:22"    **输出：** "19:22"    

**提示：**

  * `time` 的格式为 `hh:mm`
  * 题目数据保证你可以由输入的字符串生成有效的时间


**Tags:** String

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits

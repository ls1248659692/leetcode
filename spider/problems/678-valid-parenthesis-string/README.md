# [Valid Parenthesis String][title]

## Description

给定一个只包含三种字符的字符串：`（ `，`）` 和 `*`，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

  1. 任何左括号 `(` 必须有相应的右括号 `)`。
  2. 任何右括号 `)` 必须有相应的左括号 `(` 。
  3. 左括号 `(` 必须在对应的右括号之前 `)`。
  4. `*` 可以被视为单个右括号 `)` ，或单个左括号 `(` ，或一个空字符串。
  5. 一个空字符串也被视为有效字符串。

**示例 1:**
            **输入:** "()"    **输出:** True    

**示例 2:**
            **输入:** "(*)"    **输出:** True    

**示例 3:**
            **输入:** "(*))"    **输出:** True    

**注意:**

  1. 字符串大小将在 [1，100] 范围内。


**Tags:** Stack, Greedy, String, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/valid-parenthesis-string

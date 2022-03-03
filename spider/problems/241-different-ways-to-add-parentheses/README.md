# [Different Ways to Add Parentheses][title]

## Description

给你一个由数字和运算符组成的字符串 `expression` ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 **按任意顺序**
返回答案。



**示例 1：**
            **输入：** expression = "2-1-1"    **输出：** [0,2]    **解释：**    ((2-1)-1) = 0     (2-(1-1)) = 2    

**示例 2：**
            **输入：** expression = "2*3-4*5"    **输出：** [-34,-14,-10,-10,10]    **解释：**    (2*(3-(4*5))) = -34     ((2*3)-(4*5)) = -14     ((2*(3-4))*5) = -10     (2*((3-4)*5)) = -10     (((2*3)-4)*5) = 10    



**提示：**

  * `1 <= expression.length <= 20`
  * `expression` 由数字和算符 `'+'`、`'-'` 和 `'*'` 组成。
  * 输入表达式中的所有整数值在范围 `[0, 99]` 


**Tags:** Recursion, Memoization, Math, String, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/different-ways-to-add-parentheses

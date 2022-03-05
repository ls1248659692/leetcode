# [Construct Binary Tree from String][title]

## Description

你需要用一个包括括号和整数的字符串构建一棵二叉树。

输入的字符串代表一棵二叉树。它包括整数和随后的 0 、1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。

若存在子结点，则从 **左子结点** 开始构建。



**示例 1:**

![](https://assets.leetcode.com/uploads/2020/09/02/butree.jpg)
            **输入：** s = "4(2(3)(1))(6(5))"    **输出：** [4,2,6,3,1,5]    

**示例 2:**
            **输入：** s = "4(2(3)(1))(6(5)(7))"    **输出：** [4,2,6,3,1,5,7]    

**示例 3:**
            **输入：** s = "-4(2(3)(1))(6(5)(7))"    **输出：** [-4,2,6,3,1,5,7]    



**提示：**

  * `0 <= s.length <= 3 * 104`
  * 输入字符串中只包含 `'('`, `')'`, `'-'` 和 `'0'` ~ `'9'` 
  * 空树由 `""` 而非`"()"`表示。


**Tags:** Tree, Depth-First Search, String, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/construct-binary-tree-from-string

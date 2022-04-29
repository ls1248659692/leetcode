# [Check If Two Expression Trees are Equivalent][title]

## Description

**[二叉表达式树](https://en.wikipedia.org/wiki/Binary_expression_tree)**
是一种表达算术表达式的二叉树。二叉表达式树中的每一个节点都有零个或两个子节点。 叶节点（有 0 个子节点的节点）表示操作数，非叶节点（有 2
个子节点的节点）表示运算符。在本题中，我们只考虑 `'+'` 运算符（即加法）。

给定两棵二叉表达式树的根节点 `root1` 和 `root2` 。 _如果两棵二叉表达式树等价_ ，返回 `true` ，否则返回 `false` 。

当两棵二叉搜索树中的变量取任意值， **分别求得的值都相等** 时，我们称这两棵二叉表达式树是等价的。



**示例 1:**
            **输入：** root1 = [x], root2 = [x]    **输出：** true    

**示例 2:**

**![](https://assets.leetcode.com/uploads/2020/10/04/tree1.png)**
            **输入：** root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,c]    **输出：** true    **解释：** a + (b + c) == (b + c) + a

**示例 3:**

**![](https://assets.leetcode.com/uploads/2020/10/04/tree2.png)**
            **输入：** root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,d]    **输出：** false    **解释：** a + (b + c) != (b + d) + a    



**提示：**

  * 两棵树中的节点个数相等，且节点个数为范围 `[1, 4999]` 内的奇数。
  * `Node.val` 是 `'+'` 或小写英文字母。
  * 给定的树 **保证** 是有效的二叉表达式树。



**进阶：** 当你的答案需同时支持 `'-'` 运算符（减法）时，你该如何修改你的答案


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/check-if-two-expression-trees-are-equivalent

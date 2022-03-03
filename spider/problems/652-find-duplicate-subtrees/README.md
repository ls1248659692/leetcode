# [Find Duplicate Subtrees][title]

## Description

给定一棵二叉树 `root`，返回所有 **重复的子树** 。

对于同一类的重复子树，你只需要返回其中任意 **一棵** 的根结点即可。

如果两棵树具有 **相同的结构** 和 **相同的结点值** ，则它们是 **重复** 的。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/16/e1.jpg)
            **输入：** root = [1,2,3,4,null,2,4,null,null,4]    **输出：** [[2,4],[4]]

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/16/e2.jpg)
            **输入：** root = [2,1,1]    **输出：** [[1]]

**示例 3：**

**![](https://assets.leetcode.com/uploads/2020/08/16/e33.jpg)**
            **输入：** root = [2,2,2,3,null,3,null]    **输出：** [[2,3],[3]]



**提示：**

  * 树中的结点数在`[1,10^4]`范围内。
  * `-200 <= Node.val <= 200`


**Tags:** Tree, Depth-First Search, Hash Table, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/find-duplicate-subtrees

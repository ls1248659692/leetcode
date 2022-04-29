# [Binary Tree Upside Down][title]

## Description

给你一个二叉树的根节点 `root` ，请你将此二叉树上下翻转，并返回新的根节点。

你可以按下面的步骤翻转一棵二叉树：

  1. 原来的左子节点变成新的根节点
  2. 原来的根节点变成新的右子节点
  3. 原来的右子节点变成新的左子节点

![](https://assets.leetcode.com/uploads/2020/08/29/main.jpg)

上面的步骤逐层进行。题目数据保证每个右节点都有一个同级节点（即共享同一父节点的左节点）且不存在子节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/29/updown.jpg)
            **输入：** root = [1,2,3,4,5]    **输出：** [4,5,2,null,null,3,1]    

**示例 2：**
            **输入：** root = []    **输出：** []    

**示例 3：**
            **输入：** root = [1]    **输出：** [1]    



**提示：**

  * 树中节点数目在范围 `[0, 10]` 内
  * `1 <= Node.val <= 10`
  * 树中的每个右节点都有一个同级节点（即共享同一父节点的左节点）
  * 树中的每个右节点都没有子节点


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/binary-tree-upside-down

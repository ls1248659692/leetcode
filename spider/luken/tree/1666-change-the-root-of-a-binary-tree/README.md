# [Change the Root of a Binary Tree][title]

## Description

给定一棵二叉树的根节点 `root` 和一个叶节点 `leaf` ，更改二叉树，使得 `leaf` 为新的根节点。

你可以按照下列步骤修改 **从** `leaf` **到** `root` **的路径中除** `root` **外的每个节点** `cur` ：

  1. 如果 `cur` 有左子节点，则该子节点变为 `cur` 的右子节点。注意我们保证 `cur` 至多有一个子节点。
  2. `cur` 的原父节点变为 `cur` 的左子节点。

返回修改后新树的根节点。

**注意：** 确保你的答案在操作后正确地设定了 `Node.parent` （父节点）指针，否则会被判为错误答案。

**示例 1:**

![](https://assets.leetcode.com/uploads/2020/11/24/fliptree.png)
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7    **输出:** [7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]    

**示例 2:**
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0    **输出:** [0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]    

**提示:**

  * 树中节点的个数在范围 `[2, 100]` 内。
  * `-109 <= Node.val <= 109`
  * 所有的 `Node.val` 都是 **唯一** 的。
  * `leaf` 存在于树中。


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree

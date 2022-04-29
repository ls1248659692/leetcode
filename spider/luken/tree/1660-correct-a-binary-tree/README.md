# [Correct a Binary Tree][title]

## Description

你有一棵二叉树，这棵二叉树有个小问题，其中 **有且只有一个** 无效节点，它的右子节点错误地指向了与其在 **同一层** 且在其 **右侧**
的一个其他节点。

给定一棵这样的问题二叉树的根节点 `root` ，将该无效节点 **及其所有子节点移除** （除被错误指向的节点外），然后返回新二叉树的根结点。

**自定义测试用例：**

测试用例的输入由三行组成：

  * `TreeNode root`
  * `int fromNode` （在 ****`correctBinaryTree` 中 **不可见** ）
  * `int toNode` （在 ****`correctBinaryTree` 中 **不可见** ）

当以 `root` 为根的二叉树被解析后，值为 `fromNode` 的节点 `TreeNode` 将其右子节点指向值为 `toNode` 的节点
`TreeNode` 。然后， `root` 传入 `correctBinaryTree` 的参数中。

**示例 1:**

**![](https://assets.leetcode.com/uploads/2020/10/22/ex1v2.png)**
            **输入:** root = [1,2,3], fromNode = 2, toNode = 3    **输出:** [1,null,3]    **解释:** 值为 2 的节点是无效的，所以移除之。    

**示例 2:**

**![](https://assets.leetcode.com/uploads/2020/10/22/ex2v3.png)**
            **输入:** root = [8,3,1,7,null,9,4,2,null,null,null,5,6], fromNode = 7, toNode = 4    **输出:** [8,3,1,null,null,9,4,null,null,5,6]    **解释:** 值为 7 的节点是无效的，所以移除这个节点及其子节点 2。    

**提示:**

  * 树中节点个数的范围是 `[3, 104]` 。
  * `-109 <= Node.val <= 109`
  * 所有的 `Node.val` 都是 **互不相同** 的。
  * `fromNode != toNode`
  * `fromNode` 和 `toNode` 将出现在树中的同一层。
  * `toNode` 在 `fromNode` 的右侧。
  * `fromNode.right` 在测试用例的树中建立后为 `null` 。


**Tags:** Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/correct-a-binary-tree

# [Complete Binary Tree Inserter][title]

## Description

**完全二叉树** 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 `CBTInserter` 类:

  * `CBTInserter(TreeNode root)` 使用头节点为 `root` 的给定树初始化该数据结构；
  * `CBTInserter.insert(int v)`  向树中插入一个值为 `Node.val == val`的新节点 `TreeNode`。使树保持完全二叉树的状态， **并返回插入节点**  `TreeNode`  **的父节点的值** ；
  * `CBTInserter.get_root()` 将返回树的头节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg)
            **输入**    ["CBTInserter", "insert", "insert", "get_root"]    [[[1, 2]], [3], [4], []]    **输出**    [null, 1, 2, [1, 2, 3, 4]]        **解释**    CBTInserter cBTInserter = new CBTInserter([1, 2]);    cBTInserter.insert(3);  // 返回 1    cBTInserter.insert(4);  // 返回 2    cBTInserter.get_root(); // 返回 [1, 2, 3, 4]



**提示：**

  * 树中节点数量范围为 `[1, 1000]` 
  * `0 <= Node.val <= 5000`
  * `root` 是完全二叉树
  * `0 <= val <= 5000` 
  * 每个测试用例最多调用 `insert` 和 `get_root` 操作 `104` 次


**Tags:** Tree, Breadth-First Search, Design, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/complete-binary-tree-inserter

# [Closest Leaf in a Binary Tree][title]

## Description

给定一个 **每个结点的值互不相同**  的二叉树，和一个目标整数值 `k`，返回 _树中与目标值`k`  **最近的叶结点**_ 。

**与叶结点最近** __ 表示在二叉树中到达该叶节点需要行进的边数与到达其它叶结点相比最少。而且，当一个结点没有孩子结点时称其为叶结点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/13/closest1-tree.jpg)
            **输入：** root = [1, 3, 2], k = 1    **输出：** 2    **解释：** 2 和 3 都是距离目标 1 最近的叶节点。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/06/13/closest2-tree.jpg)
            **输入：** root = [1], k = 1    **输出：** 1    **解释：** 最近的叶节点是根结点自身。    

**示例 3：**

![](https://assets.leetcode.com/uploads/2021/06/13/closest3-tree.jpg)
            **输入：** root = [1,2,3,4,null,null,null,5,null,6], k = 2    **输出：** 3    **解释：** 值为 3（而不是值为 6）的叶节点是距离结点 2 的最近结点。    



**提示：**

  * 二叉树节点数在 `[1, 1000]` 范围内
  * `1 <= Node.val <= 1000`
  * 每个节点值都 **不同**
  * 给定的二叉树中有某个结点使得 `node.val == k`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/closest-leaf-in-a-binary-tree

# [Largest BST Subtree][title]

## Description

给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，并返回该子树的大小。其中，最大指的是子树节点数最多的。

**二叉搜索树（BST）** 中的所有节点都具备以下属性：

  * 左子树的值小于其父（根）节点的值。

  * 右子树的值大于其父（根）节点的值。

**注意：** 子树必须包含其所有后代。



**示例 1：**

**![](https://assets.leetcode.com/uploads/2020/10/17/tmp.jpg)**
            **输入：** root = [10,5,15,1,8,null,7]    **输出：** 3    **解释：** 本例中最大的 BST 子树是高亮显示的子树。返回值是子树的大小，即 3 。

**示例 2：**
            **输入：** root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]    **输出：** 2    



**提示：**

  * 树上节点数目的范围是 `[0, 104]`
  * `-104 <= Node.val <= 104`



**进阶:**   你能想出 O(n) 时间复杂度的解法吗？


**Tags:** Tree, Depth-First Search, Binary Search Tree, Dynamic Programming, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/largest-bst-subtree

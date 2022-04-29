# [Split BST][title]

## Description

给你一棵二叉搜索树（BST）的根结点 `root` 和一个整数 `target`
。请将该树按要求拆分为两个子树：其中一个子树结点的值都必须小于等于给定的目标值；另一个子树结点的值都必须大于目标值；树中并非一定要存在值为 `target`
的结点。

除此之外，树中大部分结构都需要保留，也就是说原始树中父节点 `p` 的任意子节点 `c` ，假如拆分后它们仍在同一个子树中，那么结点 `p` 应仍为 `c`
的父结点。

返回 _两个子树的根结点的数组_ 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/13/split-tree.jpg)
            **输入：** root = [4,2,6,1,3,5,7], target = 2    **输出：** [[2,1],[4,3,6,null,null,5,7]]    

**示例 2:**
            **输入:** root = [1], target = 1    **输出:** [[1],[]]    



**提示：**

  * 二叉搜索树节点个数在 `[1, 50]` 范围内
  * `0 <= Node.val, target <= 1000`


**Tags:** Tree, Binary Search Tree, Recursion, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/split-bst

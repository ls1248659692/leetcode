# [Binary Tree Longest Consecutive Sequence][title]

## Description

给你一棵指定的二叉树的根节点 `root` ，请你计算其中 **最长连续序列路径** 的长度。

**最长连续序列路径** 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 -
子」关系连接而产生的任意路径。且必须从父节点到子节点，反过来是不可以的。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/14/consec1-1-tree.jpg)
            **输入：** root = [1,null,3,2,4,null,null,null,5]    **输出：** 3    **解释：** 当中，最长连续序列是 3-4-5 ，所以返回结果为 3 。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/14/consec1-2-tree.jpg)
            **输入：** root = [2,null,3,2,null,1]    **输出：** 2    **解释：** 当中，最长连续序列是 2-3 。注意，不是 3-2-1，所以返回 2 。    



**提示：**

  * 树中节点的数目在范围 `[1, 3 * 104]` 内
  * `-3 * 104 <= Node.val <= 3 * 104`


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence

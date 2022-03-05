# [Depth of BST Given Insertion Order][title]

## Description

给定一个 **从 0 开始索引** 的整数类型数组 `order` ，其长度为 `n`，是从 `1` 到 `n`
的所有整数的一个排列，表示插入到一棵二叉搜索树的顺序。

二叉搜索树的定义如下：

  * 一个节点的左子树只包含键值 **小于** 该节点键值的节点。
  * 一个节点的右子树只包含键值 **大于** 该节点键值的节点。
  * 左子树和右子树须均为二叉搜索树。

该二叉搜索树的构造方式如下：

  * `order[0]` 将成为该二叉搜索树的根。
  * 所有后续的元素均在维持二叉搜索树性质的前提下作为 **任何** 已存在节点的 **子节点** 插入。

返回该二叉搜索树的 **深度** 。

一棵二叉树的 **深度** 是从根节点到最远叶节点的 **最长路径** 所经 **节点** 的个数。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/06/15/1.png)
            **输入:** order = [2,1,4,3]    **输出:** 3    **解释:** 该二叉搜索树的深度为 3，路径为 2->4->3。    

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/06/15/2.png)
            **输入:** order = [2,1,3,4]    **输出:** 3    **解释:** 该二叉搜索树的深度为 3，路径为 2->3->4。    

**示例 3:**

![](https://assets.leetcode.com/uploads/2021/06/15/3.png)
            **输入:** order = [1,2,3,4]    **输出:** 4    **解释:** 该二叉搜索树的深度为 4，路径为 1->2->3->4。    



**提示：**

  * `n == order.length`
  * `1 <= n <= 105`
  * `order` 是从 `1` 到 `n` 的整数的一个排列。


**Tags:** Tree, Binary Search Tree, Binary Tree, Ordered Set

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/depth-of-bst-given-insertion-order

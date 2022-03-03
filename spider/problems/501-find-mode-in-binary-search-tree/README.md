# [Find Mode in Binary Search Tree][title]

## Description

给你一个含重复值的二叉搜索树（BST）的根节点 `root` ，找出并返回 BST 中的所有
[众数](https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796)（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 **任意顺序** 返回。

假定 BST 满足如下定义：

  * 结点左子树中所含节点的值 **小于等于** 当前节点的值
  * 结点右子树中所含节点的值 **大于等于** 当前节点的值
  * 左子树和右子树都是二叉搜索树



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg)
            **输入：** root = [1,null,2,2]    **输出：** [2]    

**示例 2：**
            **输入：** root = [0]    **输出：** [0]    



**提示：**

  * 树中节点的数目在范围 `[1, 104]` 内
  * `-105 <= Node.val <= 105`



**进阶：** 你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/find-mode-in-binary-search-tree

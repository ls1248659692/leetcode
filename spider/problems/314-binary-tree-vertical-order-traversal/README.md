# [Binary Tree Vertical Order Traversal][title]

## Description

给你一个二叉树的根结点，返回其结点按 **垂直方向** （从上到下，逐列）遍历的结果。

如果两个结点在同一行和列，那么顺序则为  **从左到右** 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/28/vtree1.jpg)
            **输入：** root = [3,9,20,null,null,15,7]    **输出：** [[9],[3,15],[20],[7]]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/28/vtree2-1.jpg)
            **输入：** root = [3,9,8,4,0,1,7]    **输出：** [[4],[9],[3,0,1],[8],[7]]    

**示例 3：**

![](https://assets.leetcode.com/uploads/2021/01/28/vtree2.jpg)
            **输入：** root = [3,9,8,4,0,1,7,null,null,null,2,5]    **输出：** [[4],[9,5],[3,0,1],[8,2],[7]]    



**提示：**

  * 树中结点的数目在范围 `[0, 100]` 内
  * `-100 <= Node.val <= 100`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal

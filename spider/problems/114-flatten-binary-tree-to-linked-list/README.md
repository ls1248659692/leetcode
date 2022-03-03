# [Flatten Binary Tree to Linked List][title]

## Description

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

  * 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
  * 展开后的单链表应该与二叉树 [**先序遍历**](https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin) 顺序相同。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)
            **输入：** root = [1,2,5,3,4,null,6]    **输出：** [1,null,2,null,3,null,4,null,5,null,6]    

**示例 2：**
            **输入：** root = []    **输出：** []    

**示例 3：**
            **输入：** root = [0]    **输出：** [0]    

**提示：**

  * 树中结点数在范围 `[0, 2000]` 内
  * `-100 <= Node.val <= 100`

**进阶：** 你可以使用原地算法（`O(1)` 额外空间）展开这棵树吗？


**Tags:** Stack, Tree, Depth-First Search, Linked List, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list

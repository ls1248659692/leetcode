# [Binary Tree Pruning][title]

## Description

给你二叉树的根结点 `root` ，此外树的每个结点的值要么是 `0` ，要么是 `1` 。

返回移除了所有不包含 `1` 的子树的原二叉树。

节点 `node` 的子树为 `node` 本身加上所有 `node` 的后代。



**示例 1：**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)
            **输入：** root = [1,null,0,0,1]    **输出：** [1,null,0,null,1]    **解释：**    只有红色节点满足条件“所有不包含 1 的子树”。 右图为返回的答案。    

**示例 2：**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)
            **输入：** root = [1,0,1,0,0,0,1]    **输出：** [1,null,1,null,1]    

**示例 3：**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)
            **输入：** root = [1,1,0,1,1,0,1,0]    **输出：** [1,1,0,1,1,null,1]    



**提示：**

  * 树中节点的数目在范围 `[1, 200]` 内
  * `Node.val` 为 `0` 或 `1`


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/binary-tree-pruning

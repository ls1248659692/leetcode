# [Insufficient Nodes in Root to Leaf Paths][title]

## Description

给定一棵二叉树的根 `root`，请你考虑它所有  **从根到叶的路径** ：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）

假如通过节点 `node` 的每种可能的 "根-叶" 路径上值的总和全都小于给定的 `limit`，则该节点被称之为「不足节点」，需要被删除。

请你删除所有不足节点，并返回生成的二叉树的根。



**示例 1：**
            **![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-1.png)输入：** root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1    **![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-2.png)输出：** [1,2,3,4,null,null,7,8,9,null,14]    

**示例 2：**
            **![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-3.png)输入：** root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22    **![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-4.png)输出：** [5,4,8,11,null,17,4,7,null,null,null,5]

**示例 3：**
            **![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-5.png)输入：** root = [5,-6,-6], limit = 0 **输出：** []



**提示：**

  1. 给定的树有 `1` 到 `5000` 个节点
  2. `-10^5 <= node.val <= 10^5`
  3. `-10^9 <= limit <= 10^9`




**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths

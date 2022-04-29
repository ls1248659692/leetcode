# [Binary Tree Cameras][title]

## Description

给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视 **其父对象、自身及其直接子对象。**

计算监控树的所有节点所需的最小摄像头数量。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/29/bst_cameras_01.png)
            **输入：** [0,0,null,0,0]    **输出：** 1    **解释：** 如图所示，一台摄像头足以监控所有节点。    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/29/bst_cameras_02.png)
            **输入：** [0,0,null,0,null,0,null,null,0]    **输出：** 2    **解释：** 需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。    

  
**提示：**

  1. 给定树的节点数的范围是 `[1, 1000]`。
  2. 每个节点的值都是 0。


**Tags:** Tree, Depth-First Search, Dynamic Programming, Binary Tree

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/binary-tree-cameras

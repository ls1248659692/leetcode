# [Delete Tree Nodes][title]

## Description

给你一棵以节点 0 为根节点的树，定义如下：

  * 节点的总数为 `nodes` 个；
  * 第 `i` 个节点的值为 `value[i]` ；
  * 第 `i` 个节点的父节点是 `parent[i]` 。

请你删除节点值之和为 0 的每一棵子树。

在完成所有删除之后，返回树中剩余节点的数目。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/30/1421_sample_1.png)
            **输入：** nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]    **输出：** 2    

**示例 2：**
            **输入：** nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]    **输出：** 6    

**示例 3：**
            **输入：** nodes = 5, parent = [-1,0,1,0,0], value = [-672,441,18,728,378]    **输出：** 5    

**示例 4：**
            **输入：** nodes = 5, parent = [-1,0,0,1,1], value = [-686,-842,616,-739,-746]    **输出：** 5    



**提示：**

  * `1 <= nodes <= 10^4`
  * `parent.length == nodes`
  * `0 <= parent[i] <= nodes - 1`
  * `parent[0] == -1` 表示节点 `0` 是树的根。
  * `value.length == nodes`
  * `-10^5 <= value[i] <= 10^5`
  * 题目输入数据 **保证** 是一棵 **有效的树** 。


**Tags:** Tree, Depth-First Search, Breadth-First Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/delete-tree-nodes

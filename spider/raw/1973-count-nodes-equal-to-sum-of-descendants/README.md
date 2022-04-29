# [Count Nodes Equal to Sum of Descendants][title]

## Description

给定一颗二叉树的根节点 `root` ，返回满足条件：节点的值等于该节点所有子节点的值之和  _的节点的数量。_

一个节点 `x` 的  **子节点**  是指从节点 `x` 出发，到所有叶子节点路径上的节点。没有子节点的节点的子节点和视为 `0` 。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/08/17/screenshot-2021-08-17-at-17-16-50-diagram-
drawio-diagrams-net.png)
            **输入:** root = [10,3,4,2,1]    **输出:** 2    **解释:**    对于值为10的节点: 其子节点之和为： 3+4+2+1 = 10。    对于值为3的节点：其子节点之和为： 2+1 = 3。    

**示例  2:**

![](https://assets.leetcode.com/uploads/2021/08/17/screenshot-2021-08-17-at-17-25-21-diagram-
drawio-diagrams-net.png)
            **输入:** root = [2,3,null,2,null]    **输出:** 0    **解释:**    没有节点满足其值等于子节点之和。    

**示例  3:**

![](https://assets.leetcode.com/uploads/2021/08/17/screenshot-2021-08-17-at-17-23-53-diagram-
drawio-diagrams-net.png)
            **输入:** root = [0]    **输出:** 1    **解释:**    对于值为0的节点：因为它没有子节点，所以自己点之和为0。    



**提示：**

  * 树中节点的数量范围： `[1, 105]`
  * `0 <= Node.val <= 105`


**Tags:** 

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/count-nodes-equal-to-sum-of-descendants

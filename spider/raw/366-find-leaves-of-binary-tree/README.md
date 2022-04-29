# [Find Leaves of Binary Tree][title]

## Description

给你一棵二叉树，请按以下要求的顺序收集它的全部节点：

  1. 依次从左到右，每次收集并删除所有的叶子节点
  2. 重复如上过程直到整棵树为空



**示例:**
            **输入:** [1,2,3,4,5]                    1             / \            2   3           / \               4   5            **输出:** [[4,5,3],[2],[1]]    



**解释:**

1\. 删除叶子节点 `[4,5,3]` ，得到如下树结构：
                      1             /             2              



2\. 现在删去叶子节点 `[2]` ，得到如下树结构：
                      1              



3\. 现在删去叶子节点 `[1]` ，得到空树：
                      []             


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/find-leaves-of-binary-tree

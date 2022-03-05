# [Closest Binary Search Tree Value II][title]

## Description

给定二叉搜索树的根 `root` 、一个目标值 `target` 和一个整数 `k` ，返回BST中最接近目标的 `k` 个值。你可以按 **任意顺序**
返回答案。

题目  **保证**  该二叉搜索树中只会存在一种 k 个值集合最接近 `target`



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg)
            **输入:** root = [4,2,5,1,3]，目标值 = 3.714286，且 _k_ = 2    **输出:** [4,3]

**示例 2:**
            **输入:** root = [1], target = 0.000000, k = 1    **输出:** [1]    



**提示：**

  * 二叉树的节点总数为 `n`
  * `1 <= k <= n <= 104`
  * `0 <= Node.val <= 109`
  * `-109 <= target <= 109`



**进阶：** 假设该二叉搜索树是平衡的，请问您是否能在小于 `O(n)`（ `n = total nodes` ）的时间复杂度内解决该问题呢？


**Tags:** Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Tree, Heap (Priority Queue)

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii

# [Maximum Number of Accepted Invitations][title]

## Description

某一个班级有 `m` 个男孩和 `n` 个女孩，即将举行一个派对。

给定一个 `m x n` 的整数矩阵 `grid` ，其中 `grid[i][j]` 等于 `0` 或 `1` 。 若 `grid[i][j] == 1`
，则表示第 `i` 个男孩可以邀请第 `j` 个女孩参加派对。 一个男孩最多可以邀请 **一个女孩** ，一个女孩最多可以接受一个男孩的 **一个邀请**
。

返回可能的最多邀请的个数。

**示例 1:**
            **输入:** grid = [[1,1,1],                   [1,0,1],                   [0,0,1]]    **输出:** 3 **解释:** 按下列方式邀请：    - 第 1 个男孩邀请第 2 个女孩。    - 第 2 个男孩邀请第 1 个女孩。    - 第 3 个男孩邀请第 3 个女孩。

**示例 2:**
            **输入:** grid = [[1,0,1,0],                   [1,0,0,0],                   [0,0,1,0],                   [1,1,1,0]]    **输出:** 3    **解释:** 按下列方式邀请：    - 第 1 个男孩邀请第 3 个女孩。    - 第 2 个男孩邀请第 1 个女孩。    - 第 3 个男孩未邀请任何人。    - 第 4 个男孩邀请第 2 个女孩。

**提示：**

  * `grid.length == m`
  * `grid[i].length == n`
  * `1 <= m, n <= 200`
  * `grid[i][j]` 是 `0` 或 `1` 之一。


**Tags:** Array, Backtracking, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-number-of-accepted-invitations

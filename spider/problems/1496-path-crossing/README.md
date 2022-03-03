# [Path Crossing][title]

## Description

给你一个字符串 `path`，其中 `path[i]` 的值可以是 `'N'`、`'S'`、`'E'` 或者
`'W'`，分别表示向北、向南、向东、向西移动一个单位。

你从二维平面上的原点 `(0, 0)` 处开始出发，按 `path` 所指示的路径行走。

如果路径在任何位置上与自身相交，也就是走到之前已经走过的位置，请返回 `true` ；否则，返回 `false` 。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-
shot-2020-06-10-at-123929-pm.png)
            **输入：** path = "NES"    **输出：** false     **解释：** 该路径没有在任何位置相交。

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-
shot-2020-06-10-at-123843-pm.png)
            **输入：** path = "NESWW"    **输出：** true    **解释：** 该路径经过原点两次。



**提示：**

  * `1 <= path.length <= 104`
  * `path[i]` 为 `'N'`、`'S'`、`'E'` 或 `'W'`


**Tags:** Hash Table, String

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/path-crossing

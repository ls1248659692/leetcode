# [Kill Process][title]

## Description

系统中存在 `n` 个进程，形成一个有根树结构。给你两个整数数组 `pid` 和 `ppid` ，其中 `pid[i]` 是第 `i` 个进程的 ID
，`ppid[i]` 是第 `i` 个进程的父进程 ID 。

每一个进程只有 **一个父进程** ，但是可能会有 **一个或者多个子进程** 。只有一个进程的 `ppid[i] = 0` ，意味着这个进程
**没有父进程** 。

当一个进程 **被杀掉** 的时候，它所有的子进程和后代进程都要被杀掉。

给你一个整数 `kill` 表示要杀掉​​进程的 ID ，返回杀掉该进程后的所有进程 ID 的列表。可以按 **任意顺序** 返回答案。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/24/ptree.jpg)
            **输入：** pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5    **输出：** [5,10]    **解释：** 涂为红色的进程是应该被杀掉的进程。    

**示例 2：**
            **输入：** pid = [1], ppid = [0], kill = 1    **输出：** [1]    

**提示：**

  * `n == pid.length`
  * `n == ppid.length`
  * `1 <= n <= 5 * 104`
  * `1 <= pid[i] <= 5 * 104`
  * `0 <= ppid[i] <= 5 * 104`
  * 仅有一个进程没有父进程
  * `pid` 中的所有值 **互不相同**
  * 题目数据保证 `kill` 在 `pid` 中


**Tags:** Tree, Depth-First Search, Breadth-First Search, Array, Hash Table

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/kill-process

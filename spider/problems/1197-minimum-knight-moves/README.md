# [Minimum Knight Moves][title]

## Description

一个坐标可以从 `-infinity` 延伸到 `+infinity` 的 **无限大的**  棋盘上，你的 **骑士  **驻扎在坐标为 `[0, 0]`
的方格里。

骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1 格。

每次移动，他都可以按图示八个方向之一前进。

![](https://assets.leetcode.com/uploads/2018/10/12/knight.png)

返回 _骑士前去征服坐标为  `[x, y]` 的部落所需的最小移动次数_ 。本题确保答案是一定存在的。



**示例 1：**
            **输入：** x = 2, y = 1    **输出：** 1    **解释：** [0, 0] → [2, 1]    

**示例 2：**
            **输入：** x = 5, y = 5    **输出：** 4    **解释：** [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]    



**提示：**

  * `-300 <= x, y <= 300`
  * `0 <= |x| + |y| <= 300`


**Tags:** Breadth-First Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-knight-moves

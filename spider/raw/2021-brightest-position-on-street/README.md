# [Brightest Position on Street][title]

## Description

一条街上有很多的路灯，路灯的坐标由数组 `lights `的形式给出。 每个 `lights[i] = [positioni, rangei]` 代表坐标为
`positioni` 的路灯照亮的范围为 `[positioni - rangei, positioni + rangei]`  **（包括顶点）。**

位置 `p` 的亮度由能够照到 `p`的路灯的数量来决定的。

给出 `lights`, 返回 **最亮** 的位置 。如果有很多，返回坐标最小的。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/09/28/image-20210928155140-1.png)
            **输入:** lights = [[-3,2],[1,2],[3,3]]    **输出:** -1    **解释:**    第一个路灯照亮的范围是[(-3) - 2, (-3) + 2] = [-5, -1].    第二个路灯照亮的范围是 [1 - 2, 1 + 2] = [-1, 3].    第三个路灯照亮的范围是 [3 - 3, 3 + 3] = [0, 6].        坐标-1被第一个和第二个路灯照亮，亮度为2    坐标0，1，2都被第二个和第三个路灯照亮，亮度为2.    对于以上坐标，-1最小，所以返回-1

**示例 2：**
            **输入:** lights = [[1,0],[0,1]]    **输出:** 1    

**示例 3：**
            **输入:** lights = [[1,2]]    **输出:** -1    



**提示:**

  * `1 <= lights.length <= 105`
  * `lights[i].length == 2`
  * `-108 <= positioni <= 108`
  * `0 <= rangei <= 108`


**Tags:** Array, Ordered Set, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/brightest-position-on-street

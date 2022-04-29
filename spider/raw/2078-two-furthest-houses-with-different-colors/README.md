# [Two Furthest Houses With Different Colors][title]

## Description

街上有 `n` 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 **0** 开始且长度为 `n` 的整数数组 `colors` ，其中
`colors[i]` 表示第  `i` 栋房子的颜色。

返回 **两栋** 颜色 **不同** 房子之间的 **最大** 距离。

第 `i` 栋房子和第 `j` 栋房子之间的距离是 `abs(i - j)` ，其中 `abs(x)` 是 `x` 的绝对值。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/10/31/eg1.png)
            **输入：** colors = [ ** _1_** ,1,1, _ **6**_ ,1,1,1]    **输出：** 3    **解释：** 上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。    两栋颜色不同且距离最远的房子是房子 0 和房子 3 。    房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。    注意，房子 3 和房子 6 也可以产生最佳答案。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/10/31/eg2.png)
            **输入：** colors = [ _ **1**_ ,8,3,8, _ **3**_ ]    **输出：** 4    **解释：** 上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。    两栋颜色不同且距离最远的房子是房子 0 和房子 4 。    房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。    

**示例 3：**
            **输入：** colors = [ _ **0**_ , _ **1**_ ]    **输出：** 1    **解释：** 两栋颜色不同且距离最远的房子是房子 0 和房子 1 。    房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。    



**提示：**

  * `n == colors.length`
  * `2 <= n <= 100`
  * `0 <= colors[i] <= 100`
  * 生成的测试数据满足 **至少** 存在 2 栋颜色不同的房子


**Tags:** Greedy, Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_1 = 0
        n = len(colors)
        if colors[0] != colors[-1]:
                return n-1
        for i in range(1,n-1):
            if colors[i] != colors[0] or colors[i] != colors[-1]:
                max_1 = max(i-0 ,n-1-i,max_1)
        return max_1
```

[title]: https://leetcode-cn.com/problems/two-furthest-houses-with-different-colors

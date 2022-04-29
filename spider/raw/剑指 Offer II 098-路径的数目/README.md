# [路径的数目][title]

## Description

一个机器人位于一个 `m x n` _ _ 网格的左上角 （起始点在下图中标记为 "Start" ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 "Finish" ）。

问总共有多少条不同的路径？



**示例 1：**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
            **输入：** m = 3, n = 7    **输出：** 28

**示例 2：**
            **输入：** m = 3, n = 2    **输出：** 3    **解释：**    从左上角开始，总共有 3 条路径可以到达右下角。    1. 向右 -> 向下 -> 向下    2. 向下 -> 向下 -> 向右    3. 向下 -> 向右 -> 向下    

**示例 3：**
            **输入：** m = 7, n = 3    **输出：** 28    

**示例 4：**
            **输入：** m = 3, n = 3    **输出：** 6



**提示：**

  * `1 <= m, n <= 100`
  * 题目数据保证答案小于等于 `2 * 109`



注意：本题与主站 62 题相同： <https://leetcode-cn.com/problems/unique-paths/>


**Tags:** Math, Dynamic Programming, Combinatorics

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def upt(mm,nn):           
            if mm==1 or nn==1: 
                res= 1
            else: 
                res= upt(mm-1,nn)+ upt(mm,nn-1)
            return res
        return upt(m,n)        
```

[title]: https://leetcode-cn.com/problems/2AoeFn

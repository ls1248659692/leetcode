# [Valid Boomerang][title]

## Description

给定一个数组 `points` ，其中 `points[i] = [xi, yi]` 表示 **X-Y** 平面上的一个点， _如果这些点构成一个  _
**回旋镖**  则返回 `true` 。

**回旋镖**  定义为一组三个点，这些点  **各不相同**  且  **不在一条直线上**  。



**示例 1：**
            **输入：** points = [[1,1],[2,3],[3,2]]    **输出：** true    

**示例 2：**
            **输入：** points = [[1,1],[2,2],[3,3]]    **输出：** false



**提示：**

  * `points.length == 3`
  * `points[i].length == 2`
  * `0 <= xi, yi <= 100`


**Tags:** Geometry, Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # a = points[0][0]
        # b = points[1][0]
        # c = points[2][0]
        # x = points[0][1]
        # y = points[1][1]
        # z = points[2][1]
        # return True if (0.5*(a*(y-z) + b*(z-x) + c*(x-y))) != 0 else False

        s= sorted(points)
        #if s[0][0]==s[1][0]==s[2][0]: return False
        return (s[1][1]-s[0][1])  * (s[2][0]-s[0][0])!=  (s[2][1]-s[0][1]) *(s[1][0]-s[0][0])        
```

[title]: https://leetcode-cn.com/problems/valid-boomerang

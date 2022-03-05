# [Check If It Is a Straight Line][title]

## Description

给定一个数组 `coordinates` ，其中 `coordinates[i] = [x, y]` ， `[x, y]` 表示横坐标为 `x`、纵坐标为
`y` 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/10/19/untitled-diagram-2.jpg)
            **输入：** coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]    **输出：** true    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/10/19/untitled-diagram-1.jpg)**
            **输入：** coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]    **输出：** false    



**提示：**

  * `2 <= coordinates.length <= 1000`
  * `coordinates[i].length == 2`
  * `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4`
  * `coordinates` 中不含重复的点


**Tags:** Geometry, Array, Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ans = []
        coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))
        for i in range(len(coordinates)-1):
            if coordinates[i+1][0] == coordinates[i][0]:
                ans.append('zero')
            else:
                ans.append((coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0]))
        return len(set(ans)) == 1
```

[title]: https://leetcode-cn.com/problems/check-if-it-is-a-straight-line

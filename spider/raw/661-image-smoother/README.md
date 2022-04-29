# [Image Smoother][title]

## Description

**图像平滑器** 是大小为 `3 x 3` 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。

每个单元格的 **  平均灰度** 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9
个单元格的平均值）。

如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。

![](https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg)

给你一个表示图像灰度的 `m x n` 整数矩阵 `img` ，返回对图像的每个单元格平滑处理后的图像 。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg)
            **输入:** img = [[1,1,1],[1,0,1],[1,1,1]]    **输出:** [[0, 0, 0],[0, 0, 0], [0, 0, 0]]    **解释:**    对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0    对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0    对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0    

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg)
            **输入:** img = [[100,200,100],[200,50,200],[100,200,100]]    **输出:** [[137,141,137],[141,138,141],[137,141,137]]    **解释:**    对于点 (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137    对于点 (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141    对于点 (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138    



**提示:**

  * `m == img.length`
  * `n == img[i].length`
  * `1 <= m, n <= 200`
  * `0 <= img[i][j] <= 255`


**Tags:** Array, Matrix

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [ [] for i in range(len(img))]
        marginx = len(img)
        marginy = len(img[0])
        for i in range(len(img)):
            img[i].insert(0,None)
            img[i].append(None)
        img.insert(0,[None]*(marginy+2))
        img.insert(len(img),[None]*(marginy+2))
        for x in range(1,1+marginx):
            for y in range(1,1+marginy):
                surrouding_list = [img[x-1][y-1],img[x-1][y],img[x-1][y+1],img[x][y-1],img[x][y],img[x][y+1],img[x+1][y-1],img[x+1][y],img[x+1][y+1]]
                surrouding_list = [x for x in surrouding_list if x is not None]
                val_get= (sum(surrouding_list)//len(surrouding_list))
                ans[x-1].append(val_get)
        return ans
```

[title]: https://leetcode-cn.com/problems/image-smoother

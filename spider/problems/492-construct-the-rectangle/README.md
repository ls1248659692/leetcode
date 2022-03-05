# [Construct the Rectangle][title]

## Description

作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 所以，现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W
且满足以下要求的矩形的页面。要求：

  1. 你设计的矩形页面必须等于给定的目标面积。
  2. 宽度 `W` 不应大于长度 `L` ，换言之，要求 `L >= W `。
  3. 长度 `L` 和宽度 `W` 之间的差距应当尽可能小。

返回一个  _数组_  `[L, W]`，其中 _`L` 和 `W` 是你按照顺序设计的网页的长度和宽度_。  


**示例1：**
            **输入:** 4    **输出:** [2, 2]    **解释:** 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。    但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。    

**示例 2:**
            **输入:** area = 37    **输出:** [37,1]    

**示例 3:**
            **输入:** area = 122122    **输出:** [427,286]    



**提示:**

  * `1 <= area <= 107`


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area**0.5)+1,0,-1):
            if area %i==0: return [max(area//i,i),min(area//i,i)]
 
```

[title]: https://leetcode-cn.com/problems/construct-the-rectangle

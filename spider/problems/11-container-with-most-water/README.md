# [Container With Most Water][title]

## Description

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i,
height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：** 你不能倾斜容器。



**示例 1：**

![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-
upload/uploads/2018/07/25/question_11.jpg)
            **输入：** [1,8,6,2,5,4,8,3,7]    **输出：** 49     **解释：** 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

**示例 2：**
            **输入：** height = [1,1]    **输出：** 1    



**提示：**

  * `n == height.length`
  * `2 <= n <= 105`
  * `0 <= height[i] <= 104`


**Tags:** Greedy, Array, Two Pointers

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def mxa_v0(height):
            ww = len(height) - 1
            all_h_sort = sorted(list(set(height)),reverse=True)
            height_dict = {hh:set() for hh in all_h_sort}
            for ii in range(len(height)):
                height_dict[height[ii]].add(ii)
            
            water = (max(height_dict[all_h_sort[0]]) - min(height_dict[all_h_sort[0]])) * all_h_sort[0]
            wall_pool=height_dict[all_h_sort[0]]
            for hh in all_h_sort[1:]:
                if hh * ww < water: break
                wall_pool = height_dict[hh].union({min(wall_pool), max(wall_pool)})
                new_water = (max(wall_pool) - min(wall_pool)) * hh
                water = new_water if new_water > water else water
            return water

        def mxa_v1(height):
            all_h_sort = sorted(list(set(height)),reverse=True)
            height_dict = {hh:[] for hh in all_h_sort}
            for ii in range(len(height)):
                height_dict[height[ii]].append(ii)
            
            water,widthi_pool = 0,[]
            # åè®¾ hh æ¯ ä¸¤èè¾ä½çbar, æ»¡è¶³è¯¥æ¡ä»¶ä¸ç æè¿iè·ç¦»ï¼è¿­ä»£æè¿iè·ç¦»
            for hh in all_h_sort[0:]:
                widthi_pool = height_dict[hh]+([min(widthi_pool), max(widthi_pool)] if widthi_pool else [])
                new_water = (max(widthi_pool) - min(widthi_pool)) * hh
                water = new_water if new_water > water else water
            return water    
        return mxa_v1(height)        
```

[title]: https://leetcode-cn.com/problems/container-with-most-water

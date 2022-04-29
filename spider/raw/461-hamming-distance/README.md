# [Hamming Distance][title]

## Description

两个整数之间的
[汉明距离](https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB)
指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 `x` 和 `y`，计算并返回它们之间的汉明距离。

**示例 1：**
            **输入：** x = 1, y = 4    **输出：** 2    **解释：**    1   (0 0 0 1)    4   (0 1 0 0)           ↑   ↑    上面的箭头指出了对应二进制位不同的位置。    

**示例 2：**
            **输入：** x = 3, y = 1    **输出：** 1    

**提示：**

  * `0 <= x, y <= 231 - 1`


**Tags:** Bit Manipulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx =str(bin(x))[2:].zfill(32)
        yy= str(bin(y))[2:].zfill(32)
        print(xx,yy)
        return sum(1 for i in range(len(xx)) if xx[i]!=yy[i])
```

[title]: https://leetcode-cn.com/problems/hamming-distance

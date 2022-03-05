# [Can Place Flowers][title]

## Description

假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 `flowerbed` 表示花坛，由若干 `0` 和 `1` 组成，其中 `0` 表示没种植花，`1` 表示种植了花。另有一个数 `n`
**** ，能否在不打破种植规则的情况下种入 `n` **** 朵花？能则返回 `true` ，不能则返回 `false`。

**示例 1：**
            **输入：** flowerbed = [1,0,0,0,1], n = 1    **输出：** true    

**示例 2：**
            **输入：** flowerbed = [1,0,0,0,1], n = 2    **输出：** false    

**提示：**

  * `1 <= flowerbed.length <= 2 * 104`
  * `flowerbed[i]` 为 `0` 或 `1`
  * `flowerbed` 中不存在相邻的两朵花
  * `0 <= n <= flowerbed.length`


**Tags:** Greedy, Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def dsplit(s):
            r = [s[0]]
            for c in s[1:]:
                if c != r[-1][-1]:
                    r.append(c)
                else:
                    r[-1] += c
            return r    

        def v1(flowerbed):
            # r= dsplit(''.join([str(e) for e in flowerbed]))
            r= dsplit(list(map(str,flowerbed)))
            if len(r)==1 and r[0][0]=='0':return n<= (len(r[0])+1)//2
            mx0,mx1=0,0
            if r[0][0]=='0': 
                mx0=len(r[0])//2
                r = r[1:]
            if r and  r[-1][0]=='0':
                mx1=len(r[-1])//2
                r=r[:-1]
            mxr = sum([(len(z)-1)//2 for z in r if z[0]=='0'])
            return n<= mx0+mxr+mx1
        
        def v2(flowerbed):
            pass
        return v1(flowerbed)
```

[title]: https://leetcode-cn.com/problems/can-place-flowers

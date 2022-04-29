# [Heaters][title]

## Description

冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 `houses` 和供暖器 `heaters` 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

**说明** ：所有供暖器都遵循你的半径标准，加热的半径也一样。

**示例 1:**
            **输入:** houses = [1,2,3], heaters = [2]    **输出:** 1    **解释:** 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。    

**示例 2:**
            **输入:** houses = [1,2,3,4], heaters = [1,4]    **输出:** 1    **解释:** 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。    

**示例 3：**
            **输入：** houses = [1,5], heaters = [2]    **输出：** 3    

**提示：**

  * `1 <= houses.length, heaters.length <= 3 * 104`
  * `1 <= houses[i], heaters[i] <= 109`


**Tags:** Array, Two Pointers, Binary Search, Sorting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findRadius(self, ho: List[int], ha: List[int]) -> int:
        ho,ha,mir = sorted(ho),[float('-inf')]+sorted(ha),0
        while len(ha)>1 and ha[-2]>ho[-1]:ha.pop()
        while ho and len(ha)>1:
            #print('.',mir,ho,ha)

            mi=min(abs(ho[-1]-ha[-1]),abs(ho[-1]-ha[-2]))
            if mir<mi: mir = mi

            ho.pop()
      
            while ho and len(ha)>1 and ho[-1]<ha[-2]:
                ha.pop()

        
        print(mir,ho,ha)
        #if len(ha)==1: mir = max(mir,max(abs(o-ha[0]) for o in ho))
        return mir
```

[title]: https://leetcode-cn.com/problems/heaters

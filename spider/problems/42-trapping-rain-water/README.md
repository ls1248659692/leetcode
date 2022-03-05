# [Trapping Rain Water][title]

## Description

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/10/22/rainwatertrap.png)
            **输入：** height = [0,1,0,2,1,0,1,3,2,1,2,1]    **输出：** 6    **解释：** 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。     

**示例 2：**
            **输入：** height = [4,2,0,3,2,5]    **输出：** 9    



**提示：**

  * `n == height.length`
  * `1 <= n <= 2 * 104`
  * `0 <= height[i] <= 105`


**Tags:** Stack, Array, Two Pointers, Dynamic Programming, Monotonic Stack

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def trap(self, height: List[int]) -> int:
        ht= height
        res =[(ht[0],ht[0])]
        
        for h in ht[1:]:
            res.append([h,h if h>res[-1][-1] else res[-1][-1]] )
        maxh = max(el for el in height)
        tmpmx = res[-1][0]
        for i in range(len(res)-1,-1,-1):
            if res[i][0]==maxh:break
            if  res[i][0]>tmpmx:
                tmpmx= res[i][0]
            res[i][1]=tmpmx

        print(res,sum(e[1]-e[0] for e in res))
        return sum(e[1]-e[0] for e in res)

        sh = sorted([[height[i],i] for i in range(len(height))],key=lambda xx:xx[0])
        mx,mi = -1,10**9
        res=[[mx,mi]]
        for h,i in sh[::-1][:-1]:
            if i<mi:mi=i
            if i>mx:mx=i
            res.insert(0,[mi,mx])
        mg = [sh[i]+res[i] for i in range(len(sh))]
        print(len(res),len(sh),'
',mg )
        
        qli= [max(mg[j][1]-mg[j][2],mg[j][3]-mg[j][1])*mg[j][0] for j in range(len(mg)-1)]
        mg = [mg[i]+[qli[i]] for i in range(len(mg)-1)]
        print(mg)
        return max(qli)
            

        
```

[title]: https://leetcode-cn.com/problems/trapping-rain-water

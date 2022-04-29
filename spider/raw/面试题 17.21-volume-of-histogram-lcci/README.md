# [Volume of Histogram LCCI][title]

## Description

给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/10/22/rainwatertrap.png)

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。  **感谢
Marcos** 贡献此图。

**示例:**
            **输入:** [0,1,0,2,1,0,1,3,2,1,2,1]    **输出:** 6


**Tags:** Stack, Array, Two Pointers, Dynamic Programming, Monotonic Stack

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def trap(self, height: List[int]) -> int:
        ht= height
        if not ht:return 0
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

[title]: https://leetcode-cn.com/problems/volume-of-histogram-lcci

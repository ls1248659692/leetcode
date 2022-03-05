# [机器人的运动范围  LCOF][title]

## Description

地上有一个m行n列的方格，从坐标 `[0,0]` 到坐标 `[m-1,n-1]` 。一个机器人从坐标 `[0, 0]
`的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格
[35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



**示例 1：**
            **输入：** m = 2, n = 3, k = 1    **输出：** 3    

**示例 2：**
            **输入：** m = 3, n = 1, k = 0    **输出：** 1    

**提示：**

  * `1 <= n,m <= 100`
  * `0 <= k <= 20`


**Tags:** Depth-First Search, Breadth-First Search, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        aset,tset,cnt =set([(0,0)]),set([(0,0)]),1
        def dsum(i):
            c,n=0,i
            while n:
                c,n = c+n%10,n//10
            if i>10:print('.',c,i)
            return c

        while aset:
            #print(cnt,aset,tset)
            #cnt+=1
            _aset,aset=set(aset),set()
            for i,j in _aset:
                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if min(x,y)<0:continue
                    # print(i+x,j+y,m,n,k)
                    if 0<=i+x<m and 0<=j+y<n and dsum(i+x)+dsum(j+y)<=k:
                        aset.add((i+x,j+y))
                    if aset:print(i+x,j+y,m,n,aset)
            for pt in aset:tset.add(pt)
        #print('..',cnt,aset,tset)
        return len(tset)
```

[title]: https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof

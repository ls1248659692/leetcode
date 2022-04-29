# [Path with Maximum Gold][title]

## Description

你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 `m * n` 的网格 `grid`
进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 `0`。

为了使收益最大化，矿工需要按以下规则来开采黄金：

  * 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
  * 矿工每次可以从当前位置向上下左右四个方向走。
  * 每个单元格只能被开采（进入）一次。
  * **不得开采** （进入）黄金数目为 `0` 的单元格。
  * 矿工可以从网格中 **任意一个** 有黄金的单元格出发或者是停止。



**示例 1：**
            **输入：** grid = [[0,6,0],[5,8,7],[0,9,0]]    **输出：** 24    **解释：**    [[0,6,0],     [5,8,7],     [0,9,0]]    一种收集最多黄金的路线是：9 -> 8 -> 7。    

**示例 2：**
            **输入：** grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]    **输出：** 28    **解释：**    [[1,0,7],     [2,0,6],     [3,4,5],     [0,3,0],     [9,0,20]]    一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。    



**提示：**

  * `1 <= grid.length, grid[i].length <= 15`
  * `0 <= grid[i][j] <= 100`
  * 最多 **25** 个单元格中有黄金。


**Tags:** Array, Backtracking, Matrix

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def max_link(sr,sc):
            iset,isetb =set([(sr,sc)]) ,set()
            while iset != isetb:
                isetb=set(iset)
                for r,c in isetb:
                    for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if 0<=r+i<len(gd) and 0<=c+j<len(gd[0]) and gd[r+i][c+j]>0: iset.add((r+i,c+j))     
            return iset

        def islandnum(gd):
            tot1 = sum(el>0 for row in gd for el in row)
            inum ,tset,wk = 0,set(),[]
            for r in range(len(gd)):
                for c in range(len(gd[0])):
                    if gd[r][c]>0 and (r,c) not in tset:
                        inum +=1
                        iset = max_link(r,c)
                        wk.append(allwalks(iset))
                        tset =tset.union( iset)
            print('
',inum,wk)
            return inum,max(wk) if wk else 0

        def allwalks(iset):
            bdic = {(r,c):len(set([(r+1,c),(r-1,c),(r,c+1),(r,c-1)]) & iset) for r,c in iset}
            b1 = set([k for k in bdic if bdic[k]==1])
            b2 = set([k for k in bdic if bdic[k]==2])
            if len(iset)==1: return sum(gd[r][c] for r,c in iset)
            #if not b1: return sum(gd[r][c] for r,c in iset)
            isetb= set(iset)

            print(len(iset),len(isetb))
            bdic = {(r,c):len(set([(r+1,c),(r-1,c),(r,c+1),(r,c-1)]) & isetb) for r,c in isetb}   
            path_all=wak1(bdic)
            for pa in path_all:
                print([gd[r][c] for r,c in pa])
            return max(sum(gd[r][c] for r,c in path) for path in path_all)


        def wak1(bdic):
            def toend(r,c,bset,walked):
                walked2 = walked.union({(r,c)})
                inters= (set([(r+1,c),(r-1,c),(r,c+1),(r,c-1)]) & (bset-walked2))
                if inters:
                    for rn,cn in inters:
                        toend(rn,cn,bset,walked2)
                else:
                    pa.append(walked2)

            b1 = set([k for k in bdic if bdic[k]==1]) 
            b2 = set([k for k in bdic if bdic[k]==2]) 
            b3 = set([k for k in bdic if bdic[k]==3]) 
            bset = set(bdic.keys())
            print('len_b1,len_bset',len(b1),len(bset))
            path_all =[]    
            pa =[]
            if b1:
                for r,c in b1:toend(r,c,bset,set())
            elif b2:
                for r,c in b2:toend(r,c,bset,set())
            elif b3:
                for r,c in b3:toend(r,c,bset,set())                
            print('len_pa=%s'%len(pa))
            return pa

        gd=grid
        #if gd[:2]==[[1, 1, 1, 1, 1],[1, 0, 1, 0, 1]]:return 19
        for r in gd:print(r)
        return islandnum(gd)[-1]
```

[title]: https://leetcode-cn.com/problems/path-with-maximum-gold

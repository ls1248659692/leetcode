# [传递信息][title]

## Description

小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：

  1. 有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
  2. 每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
  3. 每轮信息必须需要传递给另一个人，且信息可重复经过同一个人

给定总玩家数 `n`，以及按 `[玩家编号,对应可传递玩家编号]` 关系组成的二维数组 `relation`。返回信息从小 A (编号 0 ) 经过 `k`
轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。

**示例 1：**

> 输入：`n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3`
>
> 输出：`3`
>
> 解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，分别是 0->2->0->4， 0->2->1->4，
> 0->2->3->4。

**示例 2：**

> 输入：`n = 3, relation = [[0,2],[2,1]], k = 2`
>
> 输出：`0`
>
> 解释：信息不能从小 A 处经过 2 轮传递到编号 2

**限制：**

  * `2 <= n <= 10`
  * `1 <= k <= 5`
  * `1 <= relation.length <= 90, 且 relation[i].length == 2`
  * `0 <= relation[i][0],relation[i][1] < n 且 relation[i][0] != relation[i][1]`


**Tags:** Depth-First Search, Breadth-First Search, Graph, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        def v1(n,relation,k):
            def reach(path):
                seta,tset=set([n-1]),dict({n-1:[]})
                while seta:
                    for a,b in path:
                        seta_,seta = set(seta),set()
                        if b in seta_:
                            seta.add(a)
                            for p in tset[b]:
                                p.append(a)
                return tset

            tset = reach(relation)
            print(tset)
            return min(len(pa) for pa in tset if pa[0]==0)<=k

        def v2(n,relation,k):
            def reach(path):
                seta,tset=set([n-1]),set()
                cnt =0
                while seta:
                    if cnt>k:break
                    cnt+=1
                    seta_,seta = set(seta),set()
                    for a,b in path:
                        if b in seta_:
                            seta.add(a)
                            tset.add((a,'s%d'%cnt))
                return tset
            tset = reach(relation)
            print(tset)
            pli = [1 for pa in tset if pa[0]==0 and pa[1]<='s%d'%k]
            return len(pli) if pli else 0
            
        def v3(n,relation,k):
            def reach(path):
                seta,tpa=set([n-1]),set([(n-1,)])
                cnt =0
                while seta:
                    if cnt>=k:break
                    cnt+=1
                    print(seta)
                    seta_,seta = set(seta),set()
                    for a,b in path:
                        if b in seta_:
                            seta.add(a)
                            tpa_=set(tpa)
                            for p in tpa_:
                                if p[0]==b:
                                    tpa.add(tuple([a]+list(p)))
                    
                return tpa
            tpa = reach(relation)
            print(tpa)
            # pli = [pa for pa in tpa if pa[0]==0 and len(pa)==k+1]
            pli = set([tuple(pa) for pa in tpa if pa[0]==0 and len(pa)==k+1])
            return len(pli) if pli else 0      

        def v4(n,relation,k):
            def reach(path):
                seta,tpa=set([n-1]),set([(n-1,)])
                cnt =0
                while seta:
                    if cnt>=k:break
                    cnt+=1
                    print(seta)
                    seta_,seta = set(seta),set()
                    for a,b in path:
                        if b in seta_:
                            seta.add(a)
                            seta.add((a,b))
                    tpa_,tpa=set(tpa),set()
                    for e in seta:
                        if not isinstance(e,tuple):continue
                        a,b=e
                        for p in tpa_:
                            if p[0]==b:
                                tpa.add(tuple([a]+list(p)))
                    
                return tpa
            tpa = reach(relation)
            #print(tpa)
            # pli = [pa for pa in tpa if pa[0]==0 and len(pa)==k+1]
            pli = set([tuple(pa) for pa in tpa if pa[0]==0 and len(pa)==k+1])
            return len(pli) if pli else 0
        return v4(n,relation,k)    
```

[title]: https://leetcode-cn.com/problems/chuan-di-xin-xi

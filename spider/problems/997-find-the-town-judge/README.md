# [Find the Town Judge][title]

## Description

小镇里有 `n` 个人，按从 `1` 到 `n` 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：

  1. 小镇法官不会信任任何人。
  2. 每个人（除了小镇法官）都信任这位小镇法官。
  3. 只有一个人同时满足属性 **1** 和属性 **2** 。

给你一个数组 `trust` ，其中 `trust[i] = [ai, bi]` 表示编号为 `ai` 的人信任编号为 `bi` 的人。

如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 `-1` 。



**示例 1：**
            **输入：** n = 2, trust = [[1,2]]    **输出：** 2    

**示例 2：**
            **输入：** n = 3, trust = [[1,3],[2,3]]    **输出：** 3    

**示例 3：**
            **输入：** n = 3, trust = [[1,3],[2,3],[3,1]]    **输出：** -1    



**提示：**

  * `1 <= n <= 1000`
  * `0 <= trust.length <= 104`
  * `trust[i].length == 2`
  * `trust` 中的所有`trust[i] = [ai, bi]` **互不相同**
  * `ai != bi`
  * `1 <= ai, bi <= n`


**Tags:** Graph, Array, Hash Table

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        def v1(n,trust):
            ter=set([t[0] for t in trust])
            tee=set([t[1] for t in trust])
            tli = [t[1] for t in trust]
            teem = { t:tli.count(t) for t in tee}
            teemx = {t:num for t,num in teem.items() if num==n-1}
            cz=set(list(range(1,n+1)))
            c1 = cz-ter
            c2 = c1&tee
            print('not er',c1,'be trusted',c2,'max trusted',teemx)
            lc2= list(c2)
            if n==1: return 1  if trust==[] else -1
            return lc2[0] if len(lc2)==1 and lc2[0] in teemx else -1
        return v1(n,trust)

        def v0(n,trust):
            ter=set([t[0] for t in trust])
            tee=set([t[1] for t in trust])
            cz=set(list(range(1,n+1)))
            c1 = cz-ter
            c2 = c1&tee
            print(c2)
            return list(c2)[0] if len(c2)==1 else -1            
        return v0(n,trust)
```

[title]: https://leetcode-cn.com/problems/find-the-town-judge

# [Combination Sum II][title]

## Description

给定一个候选人编号的集合 `candidates` 和一个目标数 `target` ，找出 `candidates` 中所有可以使数字和为 `target`
的组合。

`candidates` 中的每个数字在每个组合中只能使用  **一次**  。

**注意：** 解集不能包含重复的组合。



**示例  1:**
            **输入:** candidates = [10,1,2,7,6,1,5], target = 8,    **输出:**    [    [1,1,6],    [1,2,5],    [1,7],    [2,6]    ]

**示例  2:**
            **输入:** candidates = [2,5,2,1,2], target = 5,    **输出:**    [    [1,2,2],    [5]    ]



**提示:**

  * `1 <= candidates.length <= 100`
  * `1 <= candidates[i] <= 50`
  * `1 <= target <= 30`


**Tags:** Array, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def v1(candidates,target):
            def combs(clis,t):
                r =[]
                if not clis: return [[]] if  t==0 else None
                for j in range(0,2):
                    n1 = combs(clis[1:],t-j*clis[0])
                    if n1: r+= [li+[clis[0]]*j for li in n1] 
                return r
            clis = sorted(candidates,reverse=True)
            r = combs(clis,target)        
            s = set([tuple(e) for e in r])
            return [list(e) for e in s]

        def v2(candidates,target):
            def cmb(n,t):
                if len(n)==0: return [[]] if t==0 else []
                s0= cmb(n[1:],t)
                s1= [[n[0]]+e for e in cmb(n[1:],t-n[0])]
                return [e for e in s0+s1 ]
            r= cmb(candidates,target) 
            s = set([tuple(sorted(e)) for e in r])
            return [list(e) for e in s]      

        def v3(candidates,target):
            from collections import Counter
            def combs(clis,t):
                r =[]
                if not clis: return [[]] if  t==0 else []
                #print(clis,t)
                for j in range(clis[0][1]+1):
                    if t-j*clis[0][0]>=0:
                        n1 = combs(clis[1:],t-j*clis[0][0])
                        if n1: r+= [li+[clis[0][0]]*j for li in n1] 
                return r
            clis = Counter(candidates).most_common()
            #print(clis)
            #clis = sorted(candidates,reverse=True)
            r = combs(list(clis),target)        
            return r
            #s = set([tuple(e) for e in r])
            #return [list(e) for e in s] 
                      
        return v3(candidates,target)

```

[title]: https://leetcode-cn.com/problems/combination-sum-ii

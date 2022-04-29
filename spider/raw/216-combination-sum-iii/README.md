# [Combination Sum III][title]

## Description

找出所有相加之和为  _ **n** _的  ** _k  _**个数的组合 ** _。_** 组合中只允许含有 1 - 9
的正整数，并且每种组合中不存在重复的数字。

**说明：**

  * 所有数字都是正整数。
  * 解集不能包含重复的组合。 

**示例 1:**
            **输入:** _**k**_ = 3, _**n**_ = 7    **输出:** [[1,2,4]]    

**示例 2:**
            **输入:** _**k**_ = 3, _**n**_ = 9    **输出:** [[1,2,6], [1,3,5], [2,3,4]]    


**Tags:** Array, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def v3(candidates,target,k):
            from collections import Counter
            def combs(clis,t):
                r =[]
                if not clis: return [[]] if  t==0 else []
                for j in range(clis[0][1]+1):
                    if t-j*clis[0][0]>=0:
                        n1 = combs(clis[1:],t-j*clis[0][0])
                        if n1: r+= [li+[clis[0][0]]*j for li in n1] 
                return r
            clis = Counter(candidates).most_common()
            r = combs(list(clis),target)        
            return [ls for ls in r if len(ls)==k]
                      
        return v3([e for e in range(1,10)],n,k)        
```

[title]: https://leetcode-cn.com/problems/combination-sum-iii

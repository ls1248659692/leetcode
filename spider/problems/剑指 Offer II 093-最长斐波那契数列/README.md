# [最长斐波那契数列][title]

## Description

如果序列 `X_1, X_2, ..., X_n` 满足下列条件，就说它是  _斐波那契式  _的：

  * `n >= 3`
  * 对于所有 `i + 2 <= n`，都有 `X_i + X_{i+1} = X_{i+2}`

给定一个 **严格递增** 的正整数数组形成序列 `arr` ，找到 `arr` 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

_（回想一下，子序列是从原序列   `arr` 中派生出来的，它从 `arr` 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， `[3,
5, 8]` 是 `[3, 4, 5, 6, 7, 8]` 的一个子序列）_



**示例 1：**
            **输入:** arr = **** [1,2,3,4,5,6,7,8]    **输出:** 5    **解释:** 最长的斐波那契式子序列为 [1,2,3,5,8] 。    

**示例  2：**
            **输入:** arr = **** [1,3,7,11,12,14,18]    **输出:** 3    **解释** : 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。    



**提示：**

  * `3 <= arr.length <= 1000`
  * `1 <= arr[i] < arr[i + 1] <= 10^9`



注意：本题与主站 873 题相同： <https://leetcode-cn.com/problems/length-of-longest-
fibonacci-subsequence/>


**Tags:** Array, Hash Table, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        print(len(arr))
        if len(arr)>100:
            #if arr[0]==[528]:return 3
            ts=set()
            for i in range(len(arr)-2):
                k=-1
                for j in range(i+1,len(arr)-1):
                    if k==-1:k=j+1
                    f1 = arr[j]+arr[i]
                    while k<len(arr):     
                        if f1==arr[k]: 
                            ts=ts.union(set([arr[i],arr[j],arr[k]]))
                        elif arr[k]>f1:
                            break
                        k+=1
            print('len(arr)=%s,len(ts)=%s'%(len(arr),len(ts)))
            arr= sorted(list(ts))

        fbli=[]
        cac={}
        for i in range(len(arr)-2):
            knxt=-1
            for j in range(i+1,len(arr)-1):
                f1,f2,lens,cli = arr[j]+arr[i],arr[j],2,[]
                if (f1,f2) in cac:continue
                if f1>arr[-1]:continue
                k=j+1 if knxt==-1 else knxt
                while k<len(arr):
                    if f1==arr[k]:
                        cli.append((f1,f2))
                        f1,f2,lens= f1+f2,f1,lens+1
                        if lens==3: knxt=k+1
                        if (f1,f2) in cac:continue
                        if f1>arr[-1]:break
                    elif arr[k]>f1:
                        if lens==2: knxt=k
                        break
                    k+=1
                if lens>2:
                    fbli.append(lens)
                    while lens>2:
                        cac[cli.pop()] =fbli[-1]-lens
                        lens -=1
            print('cac_len=%d'%len(cac))
        return 0 if not fbli else max(fbli)        
```

[title]: https://leetcode-cn.com/problems/Q91FMA

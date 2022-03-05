# [分割回文子字符串][title]

## Description

给定一个字符串 `s` ，请将 `s` 分割成一些子串，使每个子串都是 **回文串** ，返回 s 所有可能的分割方案。

**回文串**  是正着读和反着读都一样的字符串。



**示例 1：**
            **输入：** s = **** "google"    **输出：** [["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]    

**示例 2：**
            **输入：** s = "aab"    **输出：** [["a","a","b"],["aa","b"]]    

**示例 3：**
            **输入：** s = "a"    **输出：** [["a"]]



**提示：**

  * `1 <= s.length <= 16`
  * `s `仅由小写英文字母组成



注意：本题与主站 131 题相同： <https://leetcode-cn.com/problems/palindrome-partitioning/>


**Tags:** Depth-First Search, Breadth-First Search, Graph, Hash Table

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def echo(ss):
            if ss in c2:return c2[ss]
            if len(ss)==1:
                 res=True
            else:
                res =True
                for ii in range(1, len(ss) // 2 + 1):
                    if ss[ii - 1] != ss[-ii]:
                        res=False
                        break
            c2[ss]=res
            return res

        def pt_v0(s):
            #if len(cache)>=11: return set()
            if s in cache: return cache[s]
            if len(s)==1: res= set([tuple([s,])])
            elif len(s)==2: 
                res = set([(s[0],s[1])])
                res = res.union( set([tuple([s,])]) if echo(s) else set())
            else:
                p0 =  set([tuple([s,])]) if echo(s) else set()
                p3 = set()

                for j in range(1,len(s)):
                    s1,s2=s[:j],s[j:]
                    #print('s=%s,s1=%s,pts1=%s,s2=%s,pts2=%s'%(s,s1,pt(s1),s2,pt(s2)))
                    for pt1 in pt(s1):
                        for pt2 in pt(s2):
                            p3.add( tuple(pt1 + pt2))

                res= p0.union(p3)
            cache[s]=res
            return res

        def pt(s):
            #if len(cache)>=11: return set()
            if s in cache: return cache[s]
            if len(s)==1: res= set([s])
            elif len(s)==2: 
                res = set([s[0]+'.'+s[1]])
                res = res.union( set([s]) if echo(s) else set())
            else:
                p0 =  set([s]) if echo(s) else set()
                p3 = set()
                for j in range(1,len(s)):
                    for pt1 in pt(s[:j]):
                        for pt2 in pt(s[j:]):
                            p3.add( pt1 + '.'+pt2)

                res= p0.union(p3)
            cache[s]=res
            return res

        cache={}
        c2={}
        print(len(s))
        res= pt(s)
        print(len(res),len(c2),len(cache))
        res = [e.split('.') for e in  res]
        return res

```

[title]: https://leetcode-cn.com/problems/M99OJA

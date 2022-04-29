# [Is Subsequence][title]

## Description

给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**进阶：**

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
的子序列。在这种情况下，你会怎样改变代码？

**致谢：**

特别感谢 ****[@pbrother ](https://leetcode.com/pbrother/)添加此问题并且创建所有测试用例。

**示例 1：**
            **输入：** s = "abc", t = "ahbgdc"    **输出：** true    

**示例 2：**
            **输入：** s = "axc", t = "ahbgdc"    **输出：** false    

**提示：**

  * `0 <= s.length <= 100`
  * `0 <= t.length <= 10^4`
  * 两个字符串都只由小写字符组成。


**Tags:** Two Pointers, String, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @lru_cache
        def subs(ss,ts):
            if len(ss)==1 : return [('',ts[ts.index(ss[0])+1:])] if ss[0] in ts else []
            elif len(ss)>=2:
                for i in range(len(ts)):
                    if ts[i]==ss[0]:
                        t= subs(ss[1:],ts[i+1:])
                        if t:    return t
            return []

        ss,ts =list(s),[ e for  e in list(t) if e in set(list(s))]
        return len([tt for tt in subs(''.join(ss),''.join(ts)) if not tt[0]])!=0 if ss else True
```

[title]: https://leetcode-cn.com/problems/is-subsequence

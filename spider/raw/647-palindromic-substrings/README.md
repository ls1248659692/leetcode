# [Palindromic Substrings][title]

## Description

给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

**回文字符串** 是正着读和倒过来读一样的字符串。

**子字符串** 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。



**示例 1：**
            **输入：** s = "abc"    **输出：** 3    **解释：** 三个回文子串: "a", "b", "c"    

**示例 2：**
            **输入：** s = "aaa"    **输出：** 6    **解释：** 6个回文子串: "a", "a", "a", "aa", "aa", "aaa"



**提示：**

  * `1 <= s.length <= 1000`
  * `s` 由小写英文字母组成


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        cache={'':1}
        def check_echo(s):
            for ii in range(1,len(s)//2+1):
                if s[ii-1]!=s[-ii]:return False
            return True
        liec=[]

        for i in range(len(s)-1):
            for j in range(i+2,len(s)+1):
                if j-i<2 or s[i]!=s[j-1]:continue
                if s[i+1:j-1] in cache or check_echo(s[i:j]):
                    cache[s[i:j]]=1
                    liec.append(s[i:j])
        return len(liec)+len(s)

```

[title]: https://leetcode-cn.com/problems/palindromic-substrings

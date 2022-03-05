# [Count Binary Substrings][title]

## Description

给定一个字符串 `s`，统计并返回具有相同数量 `0` 和 `1` 的非空（连续）子字符串的数量，并且这些子字符串中的所有 `0` 和所有 `1`
都是成组连续的。

重复出现（不同位置）的子串也要统计它们出现的次数。



**示例 1：**
            **输入：** s = "00110011"    **输出：** 6    **解释：** 6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。    注意，一些重复出现的子串（不同位置）要统计它们出现的次数。    另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。

**示例 2：**
            **输入：** s = "10101"    **输出：** 4    **解释：** 有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。    



**提示：**

  * `1 <= s.length <= 105`
  * `s[i]` 为 `'0'` 或 `'1'`


**Tags:** Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def v1(s):
            r = []
            ln = len(s)
            for i in range(ln):
                for j in range(i+1,ln):
                    if s[j]!=s[i]:
                        if 2*j-i<=ln and s[j:j+(j-i)] == ('1' if s[i]=='0' else '0')*(j-i):
                            r.append(s[i:2*j-i])
                        break
            #print(r)
            return len(r)

        def v2(s):
            r = 0
            ln = len(s)
            for i in range(ln):
                tk= '1' if s[i]=='0' else '0'
                for j in range(i+1,(ln+i)//2+1):
                    if s[j]!=s[i]:
                        match= True
                        for k in range(j,j+(j-i)):
                            if s[k]!=tk:
                                match=False
                                break
                        if match:r+=1
                        break
            return r

        def v3(s):
            def dsplit(s):
                r = [s[0]]
                for c in s[1:]:
                    if c != r[-1][-1]:
                        r.append(c)
                    else:
                        r[-1] += c
                return r      
            sls = dsplit(s)
            return sum(min(len(sls[i]),len(sls[i-1])) for i in range(1,len(sls)))
                      
         
        return v3(s)    

```

[title]: https://leetcode-cn.com/problems/count-binary-substrings

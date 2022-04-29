# [Reverse Substrings Between Each Pair of Parentheses][title]

## Description

给出一个字符串 `s`（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 **不应** 包含任何括号。

**示例 1：**
            **输入：** s = "(abcd)"    **输出：** "dcba"    

**示例 2：**
            **输入：** s = "(u(love)i)"    **输出：** "iloveu"    **解释：** 先反转子字符串 "love" ，然后反转整个字符串。

**示例 3：**
            **输入：** s = "(ed(et(oc))el)"    **输出：** "leetcode"    **解释：** 先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。

**示例 4：**
            **输入：** s = "a(bcdefghijkl(mno)p)q"    **输出：** "apmnolkjihgfedcbq"    

**提示：**

  * `0 <= s.length <= 2000`
  * `s` 中只有小写英文字母和括号
  * 题目测试用例确保所有括号都是成对出现的


**Tags:** Stack, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def reverseParentheses(self, s: str) -> str:
        def rp(s):
            n = 0
            pn = []
            for i in range(len(s)):
                c= s[i]
                if c=='(':n+=1
                pn.append(-n if s[i:i+2]==')(' or s[i-1:i+1]==')(' else n )
                if c==')':n-=1
            return pn

        def psplit(li):
            rli = [ [li[0],li[0]] ]
            for e in li[1:]:
                if e!=rli[-1][-1]+1: rli.append([e,e])
                else: rli[-1][-1]=e
            return rli

        while '()' in s: s= s.replace('()','')
        print(s)
        while '(' in s:
            s= s.replace('()','')
            sli = list(s)
            parli =rp(s)
            
            mx = max(parli)
            dli = [i for i in range(len(parli)) if parli[i] >=mx ]
            psli = psplit(dli)
            print('parli%s dli=%s psli=%s'%(parli,dli,psli)) 

            for b,e in psli:
                sli[b:e+1]= ['.' if el in')(' else el for el in sli[b:e+1][::-1]]
            for j  in range(len(parli)):  sli[j]='.' if parli[j]==-mx else sli[j]
                
            s= ''.join(sli).replace('.','')
            print('psli=%s,r=%s'%(psli,s))

        return s

```

[title]: https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses

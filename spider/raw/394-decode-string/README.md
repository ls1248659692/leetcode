# [Decode String][title]

## Description

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k`
保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k` ，例如不会出现像 `3a` 或 `2[4]` 的输入。



**示例 1：**
            **输入：** s = "3[a]2[bc]"    **输出：** "aaabcbc"    

**示例 2：**
            **输入：** s = "3[a2[c]]"    **输出：** "accaccacc"    

**示例 3：**
            **输入：** s = "2[abc]3[cd]ef"    **输出：** "abcabccdcdcdef"    

**示例 4：**
            **输入：** s = "abc3[cd]xyz"    **输出：** "abccdcdcdxyz"    



**提示：**

  * `1 <= s.length <= 30`
  * `s` 由小写英文字母、数字和方括号 `'[]'` 组成
  * `s` 保证是一个  **有效**  的输入。
  * `s` 中所有整数的取值范围为 `[1, 300]` 


**Tags:** Stack, Recursion, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def decodeString(self, s: str) -> str:
        pstr = s.replace('[','(1.').replace(']','.1)')
        bli = []
        brac= ''
        print('pstr=%s'%pstr)
        for ii in range(len(pstr)):
            if pstr[ii]=='(':
                brac +='('
                bli.append([ii,brac])
            elif pstr[ii]==')':
                bli.append([ii,')'*len(brac)])
                brac = brac[:-1]
        pstr_li = list(pstr)
        maxbb = '('
        for pp,bb in bli:
            pstr_li[pp]=bb[0]
            pstr_li[pp +(1 if bb[0]=='(' else -1)]= str(len(bb))
            if len(bb)>=len(maxbb) and bb[0]=='(': maxbb= '(%d'%len(bb)
        pstr = ''.join(pstr_li)
        print('maxbb=%s,pstr=%s'%(maxbb,pstr))
        #return '()'
        if maxbb=='(':return pstr
        for mm in range(int(maxbb[1:]),0,-1):
            while '(%d.'%mm in pstr:
                tmpn =''
                pstr_p1,pstr_p2 ='',''
                tmpc=''
                lastn=0
                addc =False
                ii = 0
                while ii < len(pstr)-1:
                    if pstr[ii] in '0123456789' :
                            tmpn+=pstr[ii]
                    elif pstr[ii] !='(':
                        tmpn=''
                    if pstr[ii]=='(' and pstr[ii+1]==str(mm):
                        pstr_p1 = pstr[:ii-len(tmpn)]
                        lastn=int(tmpn)
                        tmpn=''
                        ii+=1
                        addc =True
                    elif pstr[ii]==str(mm) and pstr[ii+1]==')':
                        pstr_p2 = pstr[ii+1+1:]   
                        addc=False
                        break
                    else:
                        if addc and pstr[ii]!='.': tmpc+=pstr[ii] 
                    ii +=1
                n_pstr = pstr_p1 + lastn*tmpc + pstr_p2
                #print('pstr=%s,n_pstr=%s'%(pstr,n_pstr))
                pstr = n_pstr
                #break

        #pstr = ''.join(pstr_li)
        #print(bli,pstr)
        return pstr
```

[title]: https://leetcode-cn.com/problems/decode-string

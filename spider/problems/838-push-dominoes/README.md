# [Push Dominoes][title]

## Description

`n` 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。

每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。

就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。

给你一个字符串 `dominoes` 表示这一行多米诺骨牌的初始状态，其中：

  * `dominoes[i] = 'L'`，表示第 `i` 张多米诺骨牌被推向左侧，
  * `dominoes[i] = 'R'`，表示第 `i` 张多米诺骨牌被推向右侧，
  * `dominoes[i] = '.'`，表示没有推动第 `i` 张多米诺骨牌。

返回表示最终状态的字符串。



**示例 1：**
            **输入：** dominoes = "RR.L"    **输出：** "RR.L"    **解释：** 第一张多米诺骨牌没有给第二张施加额外的力。    

**示例 2：**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png)
            **输入：** dominoes = ".L.R...LR..L.."    **输出：** "LL.RR.LLRRLL.."    



**提示：**

  * `n == dominoes.length`
  * `1 <= n <= 105`
  * `dominoes[i]` 为 `'L'`、`'R'` 或 `'.'`


**Tags:** Two Pointers, String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
def dsplit(s):
    r = [s[0]]
    for c in s[1:]:
        if ('R' in c and 'L' in r[-1]) or ('L' in c and 'R' in r[-1]):
            r.append('')
        r[-1] += c
    return r

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def tcalc(s):
            suf =  len(s)-len(s.rstrip('.'))
            return s[:len(s)-suf].replace('.',s[0])+s[len(s)-suf:]    

        def pdom(s):            
            rls =[tcalc(s) for s in dsplit(s)]
            for i in range(0,len(rls)-1):
                s= rls[i]
                if s[0]=='R':
                    suf =  len(s)-len(s.rstrip('.'))
                    rls[i]=s[:len(s)-suf]+'R'*(suf//2) +('.' if suf%2 else '') +'L'*(suf//2)
            return ''.join(rls)

        if set(list(dominoes))==set(['.']):return dominoes
        dd= dominoes.lstrip('.')
        d = dd.rstrip('.')
        return  ('L' if dd[0]=='L' else '.')*(len(dominoes)-len(dd))+ pdom(d) + ('R' if d[-1]=='R' else '.')*(len(dd)-len(d))
```

[title]: https://leetcode-cn.com/problems/push-dominoes

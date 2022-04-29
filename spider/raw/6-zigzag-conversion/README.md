# [ZigZag Conversion][title]

## Description

将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：
            P   A   H   N    A P L S I I G    Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：
            string convert(string s, int numRows);

**示例 1：**
            **输入：** s = "PAYPALISHIRING", numRows = 3    **输出：** "PAHNAPLSIIGYIR"    

**示例 2：**
            **输入：** s = "PAYPALISHIRING", numRows = 4    **输出：** "PINALSIGYAHRPI"    **解释：**    P     I    N    A   L S  I G    Y A   H R    P     I    

**示例 3：**
            **输入：** s = "A", numRows = 1    **输出：** "A"    

**提示：**

  * `1 <= s.length <= 1000`
  * `s` 由英文字母（小写和大写）、`','` 和 `'.'` 组成
  * `1 <= numRows <= 1000`


**Tags:** String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def convert(self, s: str, numRows: int) -> str:    
        nr = numRows
        unitss= numRows*2-2
        if nr==1:return s
        elif nr==2: return ''.join([s[ii] for ii in range(len(s)) if ii%2==0]) +''.join([s[ii] for ii in range(len(s)) if ii%2==1])
        elif nr==3:
            tli = []
            for r in range(nr): #4
                if r==0:tli.append([s[ii] for ii in range(len(s)) if ii%unitss==0])  
                if r==1:tli.append([s[ii] for ii in range(len(s)) if ii%unitss in [1,unitss-1]])
                if r==2:tli.append([s[ii] for ii in range(len(s)) if ii%unitss in [2]])
            return  ''.join([''.join(sub) for sub in tli])
        elif nr>=4:
            tli = []
            for r in range(nr):#6
                tli.append([s[ii] for ii in range(len(s)) if ii%unitss in [r,unitss-r]])
            return  ''.join([''.join(sub) for sub in tli])

    def convert_v1(self, s: str, numRows: int) -> str:
        if numRows==1:return s
        unitsc = numRows-1
        unitss= numRows*2-2
        li = [' ']*((int(len(s)/unitss)+1)*unitsc)
        mli = [list(li) for ii in range(numRows)]
        numCols = len(mli[0])
        pstr = s + '-'*(numRows*numCols-len(s))
        for cc in range(numCols):
            for rr in range(numRows):
                if cc%unitsc==0 and int(cc/unitsc)*unitss+rr<len(pstr):
                    mli[rr][cc]=pstr[int(cc/unitsc)*unitss+rr]
                elif rr==unitsc-cc%unitsc and int(cc/unitsc)*unitss+unitss+-rr<len(pstr):
                    mli[rr][cc]=pstr[int(cc/unitsc)*unitss+unitss-rr]
        nstr=''
        for rr in range(numRows):
            for cc in range(numCols):
                if mli[rr][cc]!=' ': nstr+= mli[rr][cc]
        return nstr.replace('-','')
```

[title]: https://leetcode-cn.com/problems/zigzag-conversion

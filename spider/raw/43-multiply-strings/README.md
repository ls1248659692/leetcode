# [Multiply Strings][title]

## Description

给定两个以字符串形式表示的非负整数 `num1` 和 `num2`，返回 `num1` 和 `num2` 的乘积，它们的乘积也表示为字符串形式。

**注意：** 不能使用任何内置的 BigInteger 库或直接将输入转换为整数。



**示例 1:**
            **输入:** num1 = "2", num2 = "3"    **输出:** "6"

**示例  2:**
            **输入:** num1 = "123", num2 = "456"    **输出:** "56088"



**提示：**

  * `1 <= num1.length, num2.length <= 200`
  * `num1` 和 `num2` 只能由数字组成。
  * `num1` 和 `num2` 都不包含任何前导零，除了数字0本身。


**Tags:** Math, String, Simulation

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1_li = [[int(num1[ii]),len(num1)-1-ii]for ii in range(len(num1))]
        n2_li = [[int(num2[ii]),len(num2)-1-ii]for ii in range(len(num2))]
        s_li = []
        for n2,n2p in n2_li:
            t_li = s_li +[[n1*n2,n1p+n2p] for n1,n1p in n1_li]
            s_li = [[0,ii] for ii in range((t_li[0][1]+1),-1,-1)]
            for tt,ttp in t_li:
                if s_li[-ttp-1][0]+tt<9: 
                   s_li[-ttp-1][0]+=tt
                else: 
                    s_li[-ttp-1-1][0]+=tt//10
                    s_li[-ttp-1][0]+=tt%10
            for kk in range(10):
                for ii in range(len(s_li)-1,-1,-1):
                    if s_li[ii][0]>=10:
                        s_li[ii-1][0]+=1
                        s_li[ii][0]-=10
            print('t_li=%s'%t_li,'s_li=%s'%s_li)
        rli = ['0']*(s_li[0][-1]+1)
        for ii in range(len(s_li)):
            rli[ii]=str(s_li[ii][0])
        res = ''.join(rli) 
        while res and res[0]=='0':res=res[1:]
        return '0' if not res else res
        
        
        

```

[title]: https://leetcode-cn.com/problems/multiply-strings

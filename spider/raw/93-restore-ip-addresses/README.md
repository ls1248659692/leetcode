# [Restore IP Addresses][title]

## Description

**有效 IP 地址** 正好由四个整数（每个整数位于 `0` 到 `255` 之间组成，且不能含有前导 `0`），整数之间用 `'.'` 分隔。

  * 例如：`"0.1.2.201"` 和` "192.168.1.1"` 是 **有效** IP 地址，但是 `"0.011.255.245"`、`"192.168.1.312"` 和 `"192.168@1.1"` 是 **无效** IP 地址。

给定一个只包含数字的字符串 `s` ，用以表示一个 IP 地址，返回所有可能的 **有效 IP 地址** ，这些地址可以通过在 `s` 中插入 `'.'`
来形成。你 **不能**  重新排序或删除 `s` 中的任何数字。你可以按 **任何** 顺序返回答案。



**示例 1：**
            **输入：** s = "25525511135"    **输出：** ["255.255.11.135","255.255.111.35"]    

**示例 2：**
            **输入：** s = "0000"    **输出：** ["0.0.0.0"]    

**示例 3：**
            **输入：** s = "101023"    **输出：** ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]    



**提示：**

  * `1 <= s.length <= 20`
  * `s` 仅由数字组成


**Tags:** String, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def __init__(self):
        self.dd = [str(el) for el in range(256)]

    def ip_p(self,pstr,n):
        #print(pstr,n)
        if n==1:
            return [pstr] if pstr in self.dd else []
        elif n>=2:
            p1,p2,p3 = [],[],[]
            if pstr[1:]: 
                p1= [pstr[:1]+'.'+el for el in self.ip_p(pstr[1:],n-1)]
                #print ('n=%s,p1=%s'%(n,p1))
            if  pstr[2:] and pstr[:2] in self.dd: 
                p2= [pstr[:2]+'.'+el for el in self.ip_p(pstr[2:],n-1)]
                #print ('n=%s,p2=%s'%(n,p2))
            if pstr[3:] and pstr[:3] in self.dd:
                p3= [pstr[:3]+'.'+el for el in self.ip_p(pstr[3:],n-1)]
                #print ('n=%s,p3=%s'%(n,p3))
            return p1+p2+p3

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.ip_p(s,4)
```

[title]: https://leetcode-cn.com/problems/restore-ip-addresses

# [Add Strings][title]

## Description

给定两个字符串形式的非负整数 `num1` 和`num2` ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 `BigInteger`）， 也不能直接将输入的字符串转换为整数形式。



**示例 1：**
            **输入：** num1 = "11", num2 = "123"    **输出：** "134"    

**示例 2：**
            **输入：** num1 = "456", num2 = "77"    **输出：** "533"    

**示例 3：**
            **输入：** num1 = "0", num2 = "0"    **输出：** "0"    





**提示：**

  * `1 <= num1.length, num2.length <= 104`
  * `num1` 和`num2` 都只包含数字 `0-9`
  * `num1` 和`num2` 都不包含任何前导零


**Tags:** Math, String, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        mt = max(len(num1),len(num2))+1
        num1,num2,r = list('0'*(mt-len(num1)) + num1),list('0'*(mt-len(num2)) + num2),['0' for i in range(mt)]
        #print(num1,num2,r)
        for i in range(1,mt):
            su = int(num1[-i])+int(num2[-i])+int(r[-i])
            
            r[-i]= str(su%10)
            r[-i-1]=str(su//10)
            #print(r,str(su%10))
        #print(r)
        res = ''.join(r)
        while len(res)>1 and res[0]=='0':res=res[1:]
        return res
```

[title]: https://leetcode-cn.com/problems/add-strings

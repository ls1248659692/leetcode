# [String to Integer (atoi)][title]

## Description

请你来实现一个 `myAtoi(string s)` 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 `atoi` 函数）。

函数 `myAtoi(string s)` 的算法如下：

  1. 读入字符串并丢弃无用的前导空格
  2. 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
  3. 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
  4. 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 `0` 。必要时更改符号（从步骤 2 开始）。
  5. 如果整数数超过 32 位有符号整数范围 `[−231,  231 − 1]` ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 `−231` 的整数应该被固定为 `−231` ，大于 `231 − 1` 的整数应该被固定为 `231 − 1` 。
  6. 返回整数作为最终结果。

**注意：**

  * 本题中的空白字符只包括空格字符 `' '` 。
  * 除前导空格或数字后的其余字符串外， **请勿忽略** 任何其他字符。



**示例  1：**
            **输入：** s = "42"    **输出：** 42    **解释：** 加粗的字符串为已经读入的字符，插入符号是当前读取的字符。    第 1 步："42"（当前没有读入字符，因为没有前导空格）             ^    第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）             ^    第 3 步：" _42_ "（读入 "42"）               ^    解析得到整数 42 。    由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。

**示例  2：**
            **输入：** s = "   -42"    **输出：** -42    **解释：**    第 1 步：" _ ****_ -42"（读入前导空格，但忽视掉）                ^    第 2 步："   _**-**_ 42"（读入 '-' 字符，所以结果应该是负数）                 ^    第 3 步："   _**-42**_ "（读入 "42"）                   ^    解析得到整数 -42 。    由于 "-42" 在范围 [-231, 231 - 1] 内，最终结果为 -42 。    

**示例  3：**
            **输入：** s = "4193 with words"    **输出：** 4193    **解释：**    第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）             ^    第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）             ^    第 3 步：" _4193_ with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）                 ^    解析得到整数 4193 。    由于 "4193" 在范围 [-231, 231 - 1] 内，最终结果为 4193 。    



**提示：**

  * `0 <= s.length <= 200`
  * `s` 由英文字母（大写和小写）、数字（`0-9`）、`' '`、`'+'`、`'-'` 和 `'.'` 组成


**Tags:** String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def myAtoi(self, s: str) -> int:
        pstr = s
        pstr=pstr.strip()
        print(','+pstr)
        negpos = 1
        maxp = str(2**31-1)
        maxn= str(2**31)
        if not pstr:return 0
        if pstr[0] not in '+-0123456789':return 0
        while pstr[0] not in '+-0123456789': pstr = pstr[1:]
        
        if pstr[0] in '+-': 
            negpos = -1 if pstr[0]== '-' else 1
            pstr= pstr[1:]
        while pstr and pstr[0]  in '0': pstr = pstr[1:]
        if not pstr or pstr[0] not in '0123456789':return 0    
       
        t_pstr = pstr
        n_pstr = ''
        for cc in t_pstr:
            if cc in '0123456789':
                n_pstr += cc
            else:
                break
        pstr = n_pstr 

        if len(pstr)<10:
            return int(pstr)*negpos
        elif len(pstr)>10:
            return 2**31-1 if negpos>0 else -2**31
        else:
            if negpos>0 and pstr>=maxp: return  2**31-1
            if negpos<0 and pstr>=maxn: return -2**31
            return negpos * int(pstr)
```

[title]: https://leetcode-cn.com/problems/string-to-integer-atoi

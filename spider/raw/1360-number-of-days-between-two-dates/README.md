# [Number of Days Between Two Dates][title]

## Description

请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 `YYYY-MM-DD`，如示例所示。



**示例 1：**
            **输入：** date1 = "2019-06-29", date2 = "2019-06-30"    **输出：** 1    

**示例 2：**
            **输入：** date1 = "2020-01-15", date2 = "2019-12-31"    **输出：** 15    



**提示：**

  * 给定的日期是 `1971` 年到 `2100` 年之间的有效日期。


**Tags:** Math, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def ndays(dt):
            #print(dt,dt[:4],dt[5:7],dt[8:])
            yy= int(dt[:4])
            yydays = (yy-1970)*365
            rn_yd = sum(1 for y in range(1970,yy) if y%4==0 and y!=2100)
            mm = int(dt[5:7])
            mmdays = sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:mm])
            rn_md = 1 if mm>=3 and yy%4==0 and yy!=2100 else 0
            dd = int(dt[8:])
            print(yy,mm,dd,yydays,mmdays,dd, rn_yd, rn_md)
            return yydays + rn_yd + mmdays + rn_md + dd

        return abs(ndays(date2)-ndays(date1))
```

[title]: https://leetcode-cn.com/problems/number-of-days-between-two-dates

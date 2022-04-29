# [Day of the Week][title]

## Description

给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：`day`、`month` 和 `year`，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 `{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
"Friday", "Saturday"}`。



**示例 1：**
            **输入：** day = 31, month = 8, year = 2019    **输出：** "Saturday"    

**示例 2：**
            **输入：** day = 18, month = 7, year = 1999    **输出：** "Sunday"    

**示例 3：**
            **输入：** day = 15, month = 8, year = 1993    **输出：** "Sunday"    



**提示：**

  * 给出的日期一定是在 `1971` 到 `2100` 年之间的有效日期。


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        w=[ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return  w[datetime.date(year,month,day).weekday()]
```

[title]: https://leetcode-cn.com/problems/day-of-the-week

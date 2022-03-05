# [Day of the Year][title]

## Description

给你一个字符串 `date` ，按 `YYYY-MM-DD` 格式表示一个
[现行公元纪年法](https://baike.baidu.com/item/公元/17855) 日期。返回该日期是当年的第几天。



**示例 1：**
            **输入：** date = "2019-01-09"    **输出：** 9    **解释：** 给定日期是2019年的第九天。

**示例 2：**
            **输入：** date = "2019-02-10"    **输出：** 41    



**提示：**

  * `date.length == 10`
  * `date[4] == date[7] == '-'`，其他的 `date[i]` 都是数字
  * `date` 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日


**Tags:** Math, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def dayOfYear(self, date: str) -> int:
        yy= date[:4]
        mm=date[5:7]
        dd=date[8:10]
        ry = int(yy)%4==0 and yy!='1900'
        mli=[0,31,28,31,30,31,30, 31,31,30,31,30,31]
        return sum(mli[:int(mm)]) + int(dd) + (1 if mm>='03' and ry else 0)
```

[title]: https://leetcode-cn.com/problems/day-of-the-year

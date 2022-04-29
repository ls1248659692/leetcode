# [Maximum Score After Splitting a String][title]

## Description

给你一个由若干 0 和 1 组成的字符串 `s` ，请你计算并返回将该字符串分割成两个 **非空** 子字符串（即  **左** 子字符串和 **右**
子字符串）所能获得的最大得分。

「分割字符串的得分」为 **左** 子字符串中 **0** 的数量加上 **右** 子字符串中 **1** 的数量。



**示例 1：**
            **输入：** s = "011101"    **输出：** 5     **解释：**    将字符串 s 划分为两个非空子字符串的可行方案有：    左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5     左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4     左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3     左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2     左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3    

**示例 2：**
            **输入：** s = "00111"    **输出：** 5    **解释：** 当 左子字符串 = "00" 且 右子字符串 = "111" 时，我们得到最大得分 = 2 + 3 = 5    

**示例 3：**
            **输入：** s = "1111"    **输出：** 3    



**提示：**

  * `2 <= s.length <= 500`
  * 字符串 `s` 仅由字符 `'0'` 和 `'1'` 组成。


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def maxScore(self, s: str) -> int:
        count_rec = 0 
        for i in range(1,len(s)):

            count = 0 
            str1 = s[0:i]
            str2 = s[i::]
            for x in str1:
                if x == '0':
                    count = count+1
            for y in str2:
                if y == '1':
                    count = count +1
            if count > count_rec:
                count_rec = count
        return count_rec
            

```

[title]: https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string

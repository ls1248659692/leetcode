# [Reverse String II][title]

## Description

给定一个字符串 `s` 和一个整数 `k`，从字符串开头算起，每计数至 `2k` 个字符，就反转这 `2k` 字符中的前 `k` 个字符。

  * 如果剩余字符少于 `k` 个，则将剩余字符全部反转。
  * 如果剩余字符小于 `2k` 但大于或等于 `k` 个，则反转前 `k` 个字符，其余字符保持原样。



**示例 1：**
            **输入：** s = "abcdefg", k = 2    **输出：** "bacdfeg"    

**示例 2：**
            **输入：** s = "abcd", k = 2    **输出：** "bacd"    



**提示：**

  * `1 <= s.length <= 104`
  * `s` 仅由小写英文组成
  * `1 <= k <= 104`


**Tags:** Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r=''.join([s[n-k:n][::-1] + s[n:n+k] for n in range(k,len(s)+k,2*k)])
        print(r)
        return s if k==1 else r if k<len(s) else s[::-1]
```

[title]: https://leetcode-cn.com/problems/reverse-string-ii

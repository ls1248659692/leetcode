# [Check if Binary String Has at Most One Segment of Ones][title]

## Description

给你一个二进制字符串 `s` ，该字符串 **不含前导零** 。

如果 `s` 包含 **零个或一个由连续的`'1'` 组成的字段** ，返回 `true`​​​ 。否则，返回 `false` 。



**示例 1：**
            **输入：** s = "1001"    **输出：** false    **解释：** 字符串中的 1 没有形成一个连续字段。    

**示例 2：**
            **输入：** s = "110"    **输出：** true



**提示：**

  * `1 <= s.length <= 100`
  * `s[i]`​​​​ 为 `'0'` 或 `'1'`
  * `s[0]` 为 `'1'`


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        def dsplit(s):
            r=[s[0]]
            for c in s[1:]:
                if c== r[-1][-1]:r[-1] += c
                else: r.append(c)
            return r
        ds = dsplit(s)
        print(ds)
        if not s:return False
        if s=='1':return True
        return len([ss for ss in ds if '1' in ss])==1

```

[title]: https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones

# [Count Substrings with Only One Distinct Letter][title]

## Description

给你一个字符串 `s`，返回 _只含 **单一字母** 的子串个数_ 。

**示例 1：**
            **输入：** s = "aaaba"    **输出：** 8    **解释：** 只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。    "aaa" 出现 1 次。    "aa" 出现 2 次。    "a" 出现 4 次。    "b" 出现 1 次。    所以答案是 1 + 2 + 4 + 1 = 8。    

**示例 2:**
            **输入：** s = "aaaaaaaaaa"    **输出：** 55    



**提示：**

  * `1 <= s.length <= 1000`
  * `s[i]` 仅由小写英文字母组成


**Tags:** Math, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countLetters(self, s: str) -> int:
        n=len(s)
        cnt=1
        total=0
        s=s+'!'
        for i in range(n):
            if s[i+1]==s[i]:
                cnt+=1
            else:
                total+=cnt*(cnt+1)//2
                cnt=1
        return total

```

[title]: https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter

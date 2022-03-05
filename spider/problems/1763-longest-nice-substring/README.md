# [Longest Nice Substring][title]

## Description

当一个字符串 `s` 包含的每一种字母的大写和小写形式 **同时** 出现在 `s` 中，就称这个字符串 `s` 是 **美好**
字符串。比方说，`"abABB"` 是美好字符串，因为 `'A'` 和 `'a'` 同时出现了，且 `'B'` 和 `'b'`
也同时出现了。然而，`"abA"` 不是美好字符串因为 `'b'` 出现了，而 `'B'` 没有出现。

给你一个字符串 `s` ，请你返回 `s` 最长的 **美好子字符串** 。如果有多个答案，请你返回 **最早**
出现的一个。如果不存在美好子字符串，请你返回一个空字符串。

**示例 1：**
            **输入：** s = "YazaAay"    **输出：** "aAa"    **解释：** "aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。    "aAa" 是最长的美好子字符串。    

**示例 2：**
            **输入：** s = "Bb"    **输出：** "Bb"    **解释：** "Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。

**示例 3：**
            **输入：** s = "c"    **输出：** ""    **解释：** 没有美好子字符串。

**示例 4：**
            **输入：** s = "dDzeE"    **输出：** "dD"    **解释：** "dD" 和 "eE" 都是最长美好子字符串。    由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。

**提示：**

  * `1 <= s.length <= 100`
  * `s` 只包含大写和小写英文字母。


**Tags:** Bit Manipulation, Hash Table, String, Sliding Window

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def v1(s):
            list_nice =[]
            length = 0 #ç»´æ¤ç¾å¥½å­ç¬¦ä¸²é¿åº¦ï¼å°½å¯è½ç¼©å°list_nice
            for i in range(len(s)):
                for k in range(i,len(s)):
                    str_probably_nice = s[i:k+1]
                    if len(set(str_probably_nice)) == 2*len(set([chr.upper() for chr in str_probably_nice])):
                        length = max(len(str_probably_nice),length)
                        if len(str_probably_nice) >= length:
                            list_nice.append(str_probably_nice)
            list_nice.sort(key = len)
            return list_nice[-1] if list_nice else ''
        
        def v0(s):
            list_nice =[]
            for i in range(len(s)):
                for k in range(i,len(s)):
                    str_probably_nice = s[i:k+1]
                    if len(set(str_probably_nice)) == 2*len(set([chr.upper() for chr in str_probably_nice])):
                        list_nice.append(str_probably_nice)
            list_nice.sort(key = len,reverse = True)
            return list_nice[0] if list_nice else ''
        
        return v0(s)



        # list =[]
        # for i in range(len(s)):
        #     for k in range(i,len(s)):
        #         list.append(s[i:k+1])
        # ans = ''
        # for i in list:
        #     if len(set([j for j in i])) == 2*len(set([j.upper() for j in i])) and len(i) > len(ans):
        #         ans = i
        # return ans
```

[title]: https://leetcode-cn.com/problems/longest-nice-substring

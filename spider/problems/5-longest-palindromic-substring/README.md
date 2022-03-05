# [Longest Palindromic Substring][title]

## Description

给你一个字符串 `s`，找到 `s` 中最长的回文子串。



**示例 1：**
            **输入：** s = "babad"    **输出：** "bab"    **解释：** "aba" 同样是符合题意的答案。    

**示例 2：**
            **输入：** s = "cbbd"    **输出：** "bb"    



**提示：**

  * `1 <= s.length <= 1000`
  * `s` 仅由数字和英文字母组成


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome_v1(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def longestPalindrome(self, s: str) -> str:
        if not s:return ''
        beg,end,ln=0,0,len(s)
        for ii in range(0,ln):
            for eo in [2,3]:
                for jj in range(0,min(ii+1,ln-ii-eo+1)): 
                    left,right = ii-jj,ii+jj+eo-1
                    if s[left]==s[right]:
                        if right-left>end-beg: beg,end=left,right
                    else:break   
        return s[beg:end+1]



        # def ispal(s,end):
        #     tend = min(end,len(s)//2+1)
        #     for ii in range(tend):
        #         if s[ii]!=s[-(ii+1)]:return False
        #     return True       

        def longestPalindrome_v0(self, s: str) -> str:
            if not s:return ''
            maxl,maxst,ln=1,s[0],len(s)
            for ii in range(0,ln):
                for eo in [2,1]:
                    fullcheck=True
                    for jj in range(0,ii+1): 
                        if jj+ii+eo<=ln and jj*2+eo>maxl:
                            if ispal(s[ii-jj:ii+jj+eo],ln if fullcheck else 1):
                                if maxl<jj*2+eo: 
                                    maxl=jj*2+eo
                                    maxst=s[ii-jj:ii+jj+eo]
                                fullcheck=False
                            else:break   
            return maxst


```

[title]: https://leetcode-cn.com/problems/longest-palindromic-substring

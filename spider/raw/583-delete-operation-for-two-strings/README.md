# [Delete Operation for Two Strings][title]

## Description

给定两个单词 `word1` 和 `word2` ，返回使得 `word1` 和  `word2` _ _ **相同** 所需的 **最小步数** 。

**每步  **可以删除任意一个字符串中的一个字符。



**示例 1：**
            **输入:** word1 = "sea", word2 = "eat"    **输出:** 2    **解释:** 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"    

**示例  2:**
            **输入：** word1 = "leetcode", word2 = "etco"    **输出：** 4    



**提示：**

  * `1 <= word1.length, word2.length <= 500`
  * `word1` 和 `word2` 只包含小写英文字母


**Tags:** String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def longsq(text1,text2):
            m,n= len(text1),len(text2)
            dp = [[0 ]*(n+1) for _ in range(1+m)]
            for i in range(1,1+m):
                for j in range(1,1+n):
                    dp[i][j] = max(dp[i-1][j] ,dp[i][j-1] ,dp[i-1][j-1] +(text1[i-1] == text2[j-1]))
            # return max([e for row in dp for e in row]) 
            return dp[-1][-1]

        wa,wb = (word2,word1)if len(word1)<len(word2) else (word1,word2)      
        lna,lnb= len(wa),len(wb)
        return lna+lnb-2*longsq(wa,wb)                   
```

[title]: https://leetcode-cn.com/problems/delete-operation-for-two-strings

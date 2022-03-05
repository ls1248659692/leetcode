# [Maximum Product of Word Lengths][title]

## Description

给你一个字符串数组 `words` ，找出并返回 `length(words[i]) * length(words[j])`
的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 `0` 。



**示例  1：**
            **输入：** words = ["abcw","baz","foo","bar","xtfn","abcdef"]    **输出：**16     **解释** **：**这两个单词为 **** "abcw", "xtfn"。

**示例 2：**
            **输入：** words = ["a","ab","abc","d","cd","bcd","abcd"]    **输出：**4     **解释** **：** 这两个单词为 "ab", "cd"。

**示例 3：**
            **输入：** words = ["a","aa","aaa","aaaa"]    **输出：**0     **解释** **：**不存在这样的两个单词。    



**提示：**

  * `2 <= words.length <= 1000`
  * `1 <= words[i].length <= 1000`
  * `words[i]` 仅包含小写字母


**Tags:** Bit Manipulation, Array, String

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ts=[(set(list(wd)),len(wd)) for wd in words]
        ts = sorted(ts,key=lambda xx:xx[1],reverse=True)
        maxl=0
        ln =len(ts)
        #print(ts)
        for i in range(ln):
            if ts[i][1]**2<maxl:break
            for j in range(i+1,ln):
                if not ts[i][0].intersection(ts[j][0]):
                    #print(ts[i],ts[j])
                    prd = ts[i][1]*ts[j][1]
                    if prd>maxl: maxl=prd
                    break
        return maxl
```

[title]: https://leetcode-cn.com/problems/maximum-product-of-word-lengths

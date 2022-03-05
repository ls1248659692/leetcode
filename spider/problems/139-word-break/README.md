# [Word Break][title]

## Description

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。请你判断是否可以利用字典中出现的单词拼接出 `s` 。

**注意：** 不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。



**示例 1：**
            **输入:** s = "leetcode", wordDict = ["leet", "code"]    **输出:** true    **解释:** 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。    

**示例 2：**
            **输入:** s = "applepenapple", wordDict = ["apple", "pen"]    **输出:** true    **解释:** 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。         注意，你可以重复使用字典中的单词。    

**示例 3：**
            **输入:** s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]    **输出:** false    



**提示：**

  * `1 <= s.length <= 300`
  * `1 <= wordDict.length <= 1000`
  * `1 <= wordDict[i].length <= 20`
  * `s` 和 `wordDict[i]` 仅有小写英文字母组成
  * `wordDict` 中的所有字符串 **互不相同**


**Tags:** Trie, Memoization, Hash Table, String, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def __init__(self):
        self.init_wdic  = []
        self.wdmin =0
        self.wdmax= 20
        self.cache={}

    def wb(self,s):
        if s in self.cache: return self.cache[s]
        
        if s in self.init_wdic: 
            r='o'
        else:
            rli=['']*20
            for ii in range(self.wdmin,self.wdmax):
                #print(s[:ii],s[ii:])
                if s[:ii] in self.init_wdic:
                    rli[ii]+=self.wb(s[ii:])
            if ''.join(rli)=='': r= 'f'
            elif 'o' in rli: r= 'o'
            else: r= 'f'
        self.cache[s]=r
        return r
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not self.init_wdic: 
            self.init_wdic=wordDict
            self.wdmin = min([len(el) for el in wordDict])
            self.wdmax = max(self.wdmin+1,max([len(el)+1 for el in wordDict]))
            print(self.wdmin,self.wdmax)
        return self.wb(s)=='o'


```

[title]: https://leetcode-cn.com/problems/word-break

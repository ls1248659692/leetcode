# [Sparse Array Search LCCI][title]

## Description

稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

**示例1:**
            **输入** : words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"    **输出** ：-1    **说明** : 不存在返回-1。    

**示例2:**
            **输入** ：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"    **输出** ：4    

**提示:**

  1. words的长度在[1, 1000000]之间


**Tags:** Array, String, Binary Search

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i in range(len(words)):
            if words[i]: 
                if words[i]<s:continue
                elif words[i]==s:return i
                else:break
        return -1

```

[title]: https://leetcode-cn.com/problems/sparse-array-search-lcci

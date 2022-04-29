# [Sort Characters By Frequency][title]

## Description

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

**示例 1:**
            **输入:**    "tree"        **输出:**    "eert"        **解释:** 'e'出现两次，'r'和't'都只出现一次。    因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。    

**示例 2:**
            **输入:**    "cccaaa"        **输出:**    "cccaaa"        **解释:** 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。    注意"cacaca"是不正确的，因为相同的字母必须放在一起。    

**示例 3:**
            **输入:**    "Aabb"        **输出:**    "bbAa"        **解释:** 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。    注意'A'和'a'被认为是两种不同的字符。    


**Tags:** Hash Table, String, Bucket Sort, Counting, Sorting, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def frequencySort(self, s: str) -> str:
        ds = {c:s.count(c) for c in set(list(s))}
        st = sorted(ds.items(),key=lambda xx:xx[1],reverse=True)
        return ''.join([e[0]*e[1] for e in st])
```

[title]: https://leetcode-cn.com/problems/sort-characters-by-frequency

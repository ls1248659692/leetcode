# [Top K Frequent Words][title]

## Description

给定一个单词列表 `words` 和一个整数 `k` ，返回前 `k` _ _ 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， **按字典顺序** 排序。



**示例 1：**
            **输入:** words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2    **输出:** ["i", "love"]    **解析:** "i" 和 "love" 为出现次数最多的两个单词，均为2次。        注意，按字母顺序 "i" 在 "love" 之前。    

**示例 2：**
            **输入:** ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4    **输出:** ["the", "is", "sunny", "day"]    **解析:** "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，        出现次数依次为 4, 3, 2 和 1 次。    



**注意：**

  * `1 <= words.length <= 500`
  * `1 <= words[i] <= 10`
  * `words[i]` 由小写英文字母组成。
  * `k` 的取值范围是 `[1, **不同** words[i] 的数量]`



**进阶：** 尝试以 `O(n log k)` 时间复杂度和 `O(n)` 空间复杂度解决。


**Tags:** Trie, Hash Table, String, Bucket Sort, Counting, Sorting, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [el[0] for el in sorted({wd:words.count(wd) for wd in set(words)}.items(),key=lambda xx:str(99999-xx[1])+xx[0],reverse=False)][:k]
        dic = {wd:words.count(wd) for wd in set(words)}
        srt = sorted(dic.items(),key=lambda xx:str(99999-xx[1])+xx[0],reverse=False)
        return [el[0] for el in srt][:k]
```

[title]: https://leetcode-cn.com/problems/top-k-frequent-words

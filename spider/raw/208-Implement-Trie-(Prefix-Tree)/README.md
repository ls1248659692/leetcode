# [Implement Trie (Prefix Tree)][title]

## Description

**[Trie](https://baike.baidu.com/item/字典树/9825209?fr=aladdin)** （发音类似
"try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

  * `Trie()` 初始化前缀树对象。
  * `void insert(String word)` 向前缀树中插入字符串 `word` 。
  * `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
  * `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

**示例：**
            **输入**    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]    **输出**    [null, null, true, false, true, null, true]        **解释**    Trie trie = new Trie();    trie.insert("apple");    trie.search("apple");   // 返回 True    trie.search("app");     // 返回 False    trie.startsWith("app"); // 返回 True    trie.insert("app");    trie.search("app");     // 返回 True    

**提示：**

  * `1 <= word.length, prefix.length <= 2000`
  * `word` 和 `prefix` 仅由小写英文字母组成
  * `insert`、`search` 和 `startsWith` 调用次数 **总计** 不超过 `3 * 104` 次


**Tags:** Design, Trie, Hash Table, String

**Difficulty:** Medium

## 思路

``` python3
class Trie:

    def __init__(self):
        self.wset=set()
        self.abdic=dict()


    def insert(self, word: str) -> None:
        self.wset.add(word)
        self.abdic.setdefault(word[0],{})
        if len(word)>1:
            self.abdic[word[0]].setdefault(word[1],[])
            self.abdic[word[0]][word[1]].append(word)
        else:
            self.abdic[word[0]].setdefault(word,{})

    def search(self, word: str) -> bool:
        return word in self.wset


    def startsWith(self, prefix: str) -> bool:
        if len(prefix)==1: return prefix in self.abdic
        elif len(prefix)==2: return prefix[0] in self.abdic and prefix[1] in self.abdic[prefix[0]]
        else:
            if prefix[0] in self.abdic and prefix[1] in self.abdic[prefix[0]]:
                for wd in self.abdic[prefix[0]][prefix[1]]:
                    if len(prefix)<=len(wd) and wd[:len(prefix)]==prefix:return True
            return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

[title]: https://leetcode-cn.com/problems/implement-trie-prefix-tree

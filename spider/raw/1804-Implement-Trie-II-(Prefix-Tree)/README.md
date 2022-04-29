# [Implement Trie II (Prefix Tree)][title]

## Description

前缀树（ **[trie](https://en.wikipedia.org/wiki/Trie)** ，发音为
"try"）是一个树状的数据结构，用于高效地存储和检索一系列字符串的前缀。前缀树有许多应用，如自动补全和拼写检查。

实现前缀树 Trie 类：

  * `Trie()` 初始化前缀树对象。
  * `void insert(String word)` 将字符串 `word` 插入前缀树中。
  * `int countWordsEqualTo(String word)` 返回前缀树中字符串 `word` 的实例个数。
  * `int countWordsStartingWith(String prefix)` 返回前缀树中以 `prefix` 为前缀的字符串个数。
  * `void erase(String word)` 从前缀树中移除字符串 `word` 。

**示例 1:**
            **输入**    ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]    [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]    **输出**    [null, null, null, 2, 2, null, 1, 1, null, 0]        **解释**    Trie trie = new Trie();    trie.insert("apple");               // 插入 "apple"。    trie.insert("apple");               // 插入另一个 "apple"。    trie.countWordsEqualTo("apple");    // 有两个 "apple" 实例，所以返回 2。    trie.countWordsStartingWith("app"); // "app" 是 "apple" 的前缀，所以返回 2。    trie.erase("apple");                // 移除一个 "apple"。    trie.countWordsEqualTo("apple");    // 现在只有一个 "apple" 实例，所以返回 1。    trie.countWordsStartingWith("app"); // 返回 1    trie.erase("apple");                // 移除 "apple"。现在前缀树是空的。    trie.countWordsStartingWith("app"); // 返回 0    

**提示：**

  * `1 <= word.length, prefix.length <= 2000`
  * `word` 和 `prefix` 只包含小写英文字母。
  * `insert`、 `countWordsEqualTo`、 `countWordsStartingWith` 和 `erase` **总共** 调用最多 `3 * 104` 次。
  * 保证每次调用 `erase` 时，字符串 `word` 总是存在于前缀树中。


**Tags:** Design, Trie, Hash Table, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/implement-trie-ii-prefix-tree

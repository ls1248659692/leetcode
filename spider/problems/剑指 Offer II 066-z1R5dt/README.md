# [单词之和][title]

## Description

实现一个 `MapSum` 类，支持两个方法，`insert` 和 `sum`：

  * `MapSum()` 初始化 `MapSum` 对象
  * `void insert(String key, int val)` 插入 `key-val` 键值对，字符串表示键 `key` ，整数表示值 `val` 。如果键 `key` 已经存在，那么原来的键值对将被替代成新的键值对。
  * `int sum(string prefix)` 返回所有以该前缀 `prefix` 开头的键 `key` 的值的总和。



**示例：**
            **输入：**    inputs = ["MapSum", "insert", "sum", "insert", "sum"]    inputs = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]    **输出：**    [null, null, 3, null, 5]        **解释：**    MapSum mapSum = new MapSum();    mapSum.insert("apple", 3);      mapSum.sum("ap");           // return 3 ( _ap_ ple = 3)    mapSum.insert("app", 2);        mapSum.sum("ap");           // return 5 ( _ap_ ple + _ap_ p = 3 + 2 = 5)    



**提示：**

  * `1 <= key.length, prefix.length <= 50`
  * `key` 和 `prefix` 仅由小写英文字母组成
  * `1 <= val <= 1000`
  * 最多调用 `50` 次 `insert` 和 `sum`



注意：本题与主站 677 题相同： <https://leetcode-cn.com/problems/map-sum-pairs/>


**Tags:** Design, Trie, Hash Table, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/z1R5dt

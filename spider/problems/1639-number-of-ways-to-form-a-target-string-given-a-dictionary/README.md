# [Number of Ways to Form a Target String Given a Dictionary][title]

## Description

给你一个字符串列表 `words` 和一个目标字符串 `target` 。`words` 中所有字符串都 **长度相同** 。

你的目标是使用给定的 `words` 字符串列表按照下述规则构造 `target` ：

  * 从左到右依次构造 `target` 的每一个字符。
  * 为了得到 `target` 第 `i` 个字符（下标从 **0** 开始），当 `target[i] = words[j][k]` 时，你可以使用 `words` 列表中第 `j` 个字符串的第 `k` 个字符。
  * 一旦你使用了 `words` 中第 `j` 个字符串的第 `k` 个字符，你不能再使用 `words` 字符串列表中任意单词的第 `x` 个字符（`x <= k`）。也就是说，所有单词下标小于等于 `k` 的字符都不能再被使用。
  * 请你重复此过程直到得到目标字符串 `target` 。

**请注意** ， 在构造目标字符串的过程中，你可以按照上述规定使用 `words` 列表中 **同一个字符串** 的 **多个字符** 。

请你返回使用 `words` 构造 `target` 的方案数。由于答案可能会很大，请对 `109 + 7` **取余** 后返回。

（译者注：此题目求的是有多少个不同的 `k` 序列，详情请见示例。）

**示例 1：**
            **输入：** words = ["acca","bbbb","caca"], target = "aba"    **输出：** 6    **解释：** 总共有 6 种方法构造目标串。    "aba" -> 下标为 0 (" **a** cca")，下标为 1 ("b **b** bb")，下标为 3 ("cac **a** ")    "aba" -> 下标为 0 (" **a** cca")，下标为 2 ("bb **b** b")，下标为 3 ("cac **a** ")    "aba" -> 下标为 0 (" **a** cca")，下标为 1 ("b **b** bb")，下标为 3 ("acc **a** ")    "aba" -> 下标为 0 (" **a** cca")，下标为 2 ("bb **b** b")，下标为 3 ("acc **a** ")    "aba" -> 下标为 1 ("c **a** ca")，下标为 2 ("bb **b** b")，下标为 3 ("acc **a** ")    "aba" -> 下标为 1 ("c **a** ca")，下标为 2 ("bb **b** b")，下标为 3 ("cac **a** ")    

**示例 2：**
            **输入：** words = ["abba","baab"], target = "bab"    **输出：** 4    **解释：** 总共有 4 种不同形成 target 的方法。    "bab" -> 下标为 0 (" **b** aab")，下标为 1 ("b **a** ab")，下标为 2 ("ab **b** a")    "bab" -> 下标为 0 (" **b** aab")，下标为 1 ("b **a** ab")，下标为 3 ("baa **b** ")    "bab" -> 下标为 0 (" **b** aab")，下标为 2 ("ba **a** b")，下标为 3 ("baa **b** ")    "bab" -> 下标为 1 ("a **b** ba")，下标为 2 ("ba **a** b")，下标为 3 ("baa **b** ")    

**示例 3：**
            **输入：** words = ["abcd"], target = "abcd"    **输出：** 1    

**示例 4：**
            **输入：** words = ["abab","baba","abba","baab"], target = "abba"    **输出：** 16    

**提示：**

  * `1 <= words.length <= 1000`
  * `1 <= words[i].length <= 1000`
  * `words` 中所有单词长度相同。
  * `1 <= target.length <= 1000`
  * `words[i]` 和 `target` 都仅包含小写英文字母。


**Tags:** Array, String, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary

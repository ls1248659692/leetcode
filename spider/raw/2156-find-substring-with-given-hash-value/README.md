# [Find Substring With Given Hash Value][title]

## Description

给定整数 `p` 和 `m` ，一个长度为 `k` 且下标从 **0**  开始的字符串 `s` 的哈希值按照如下函数计算：

  * `hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m`.

其中 `val(s[i])` 表示 `s[i]` 在字母表中的下标，从 `val('a') = 1` 到 `val('z') = 26` 。

给你一个字符串 `s` 和整数 `power`，`modulo`，`k` 和 `hashValue` 。请你返回 `s` 中 **第一个** 长度为 `k`
的 **子串**  `sub` ，满足 _ _`hash(sub, power, modulo) == hashValue` 。

测试数据保证一定 **存在**  至少一个这样的子串。

**子串** 定义为一个字符串中连续非空字符组成的序列。



**示例 1：**
            **输入：** s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0    **输出：** "ee"    **解释：** "ee" 的哈希值为 hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0 。    "ee" 是长度为 2 的第一个哈希值为 0 的子串，所以我们返回 "ee" 。    

**示例 2：**
            **输入：** s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32    **输出：** "fbx"    **解释：** "fbx" 的哈希值为 hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 312) mod 100 = 23132 mod 100 = 32 。    "bxz" 的哈希值为 hash("bxz", 31, 100) = (2 * 1 + 24 * 31 + 26 * 312) mod 100 = 25732 mod 100 = 32 。    "fbx" 是长度为 3 的第一个哈希值为 32 的子串，所以我们返回 "fbx" 。    注意，"bxz" 的哈希值也为 32 ，但是它在字符串中比 "fbx" 更晚出现。    



**提示：**

  * `1 <= k <= s.length <= 2 * 104`
  * `1 <= power, modulo <= 109`
  * `0 <= hashValue < modulo`
  * `s` 只包含小写英文字母。
  * 测试数据保证一定 **存在**  满足条件的子串。


**Tags:** String, Sliding Window, Hash Function, Rolling Hash

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/find-substring-with-given-hash-value

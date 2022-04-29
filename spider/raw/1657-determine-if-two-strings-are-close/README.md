# [Determine if Two Strings Are Close][title]

## Description

如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 **接近** ：

  * 操作 1：交换任意两个 **现有** 字符。     * 例如，`a **b** cd **e** -> a **e** cd **b**`
  * 操作 2：将一个 **现有** 字符的每次出现转换为另一个 **现有** 字符，并对另一个字符执行相同的操作。     * 例如，` **aa** c **abb** -> **bb** c **baa**`（所有 `a` 转化为 `b` ，而所有的 `b` 转换为 `a` ）

你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，`word1` 和 `word2` 。如果 __`word1` __ 和 __`word2` __**接近** ，就返回 `true`
；否则，返回 __`false` __ 。

**示例 1：**
            **输入：** word1 = "abc", word2 = "bca"    **输出：** true    **解释：** 2 次操作从 word1 获得 word2 。    执行操作 1："a **bc** " -> "a **cb** "    执行操作 1：" **a** c **b** " -> " **b** c **a** "    

**示例 2：**
            **输入：** word1 = "a", word2 = "aa"    **输出：** false    **解释：** 不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。

**示例 3：**
            **输入：** word1 = "cabbba", word2 = "abbccc"    **输出：** true    **解释：** 3 次操作从 word1 获得 word2 。    执行操作 1："ca **b** bb **a** " -> "ca **a** bb **b** "    执行操作 2：" **c** aa **bbb** " -> " **b** aa **ccc** "    执行操作 2：" **baa** ccc" -> " **abb** ccc"    

**示例 4：**
            **输入：** word1 = "cabbba", word2 = "aabbss"    **输出：** false    **解释：** 不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。

**提示：**

  * `1 <= word1.length, word2.length <= 105`
  * `word1` 和 `word2` 仅包含小写英文字母


**Tags:** Hash Table, String, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/determine-if-two-strings-are-close

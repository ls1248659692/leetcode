# [Pattern Matching LCCI][title]

## Description

你有两个字符串，即`pattern`和`value`。
`pattern`字符串由字母`"a"`和`"b"`组成，用于描述字符串中的模式。例如，字符串`"catcatgocatgo"`匹配模式`"aabab"`（其中`"cat"`是`"a"`，`"go"`是`"b"`），该字符串也匹配像`"a"`、`"ab"`和`"b"`这样的模式。但需注意`"a"`和`"b"`不能同时表示相同的字符串。编写一个方法判断`value`字符串是否匹配`pattern`字符串。

**示例 1：**
            **输入：** pattern = "abba", value = "dogcatcatdog"    **输出：** true    

**示例 2：**
            **输入：** pattern = "abba", value = "dogcatcatfish"    **输出：** false    

**示例 3：**
            **输入：** pattern = "aaaa", value = "dogcatcatdog"    **输出：** false    

**示例 4：**
            **输入：** pattern = "abba", value = "dogdogdogdog"    **输出：** true    **解释：** "a"="dogdog",b=""，反之也符合规则    

**提示：**

  * `1 <= len(pattern) <= 1000`
  * `0 <= len(value) <= 1000`
  * 你可以假设`pattern`只包含字母`"a"`和`"b"`，`value`仅包含小写字母。


**Tags:** Math, String, Backtracking, Enumeration

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/pattern-matching-lcci

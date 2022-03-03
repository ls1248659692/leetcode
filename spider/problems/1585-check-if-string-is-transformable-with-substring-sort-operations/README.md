# [Check If String Is Transformable With Substring Sort Operations][title]

## Description

给你两个字符串 `s` 和 `t` ，请你通过若干次以下操作将字符串 `s` 转化成字符串 `t` ：

  * 选择 `s` 中一个 **非空**  子字符串并将它包含的字符就地 **升序**  排序。

比方说，对下划线所示的子字符串进行操作可以由 `"1 **4234** "` 得到 `"1 **2344** "` 。

如果可以将字符串 `s` 变成 `t` ，返回 `true` 。否则，返回 `false` 。

一个 **子字符串**  定义为一个字符串中连续的若干字符。



**示例 1：**
            **输入：** s = "84532", t = "34852"    **输出：** true    **解释：** 你可以按以下操作将 s 转变为 t ：    "84 **53** 2" （从下标 2 到下标 3）-> "84 **35** 2"    " **843** 52" （从下标 0 到下标 2） -> " **348** 52"    

**示例 2：**
            **输入：** s = "34521", t = "23415"    **输出：** true    **解释：** 你可以按以下操作将 s 转变为 t ：    " **3452** 1" -> " **2345** 1"    "234 **51** " -> "234 **15** "    

**示例 3：**
            **输入：** s = "12345", t = "12435"    **输出：** false    

**示例 4：**
            **输入：** s = "1", t = "2"    **输出：** false    



**提示：**

  * `s.length == t.length`
  * `1 <= s.length <= 105`
  * `s` 和 `t` 都只包含数字字符，即 `'0'` 到 `'9'` 。


**Tags:** Greedy, String, Sorting

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/check-if-string-is-transformable-with-substring-sort-operations

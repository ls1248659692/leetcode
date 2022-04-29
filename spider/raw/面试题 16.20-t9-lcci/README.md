# [T9 LCCI][title]

## Description

在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你会得到一张含有有效单词的列表。映射如下图所示：

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/original_images/17_telephone_keypad.png)

**示例 1:**
            **输入:** num = "8733", words = ["tree", "used"]    **输出:** ["tree", "used"]    

**示例 2:**
            **输入:** num = "2", words = ["a", "b", "c", "d"]    **输出:** ["a", "b", "c"]

提示：

  * `num.length <= 1000`
  * `words.length <= 500`
  * `words[i].length == num.length`
  * `num`中不会出现 0, 1 这两个数字


**Tags:** Array, Hash Table, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/t9-lcci

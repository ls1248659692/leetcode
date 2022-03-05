# [Next Palindrome Using Same Digits][title]

## Description

给你一个很长的数字回文串 `num` ，返回 **大于** `num`、 **由相同数字重新组合而成的最小** 回文串。

如果不存在这样的回文串，则返回空串 `""`。

**回文串** 是正读和反读都一样的字符串。

**示例 1：**
            **输入：** num = "1221"    **输出：** "2112"    **解释：** 下个比 **** "1221" 大的回文串是 "2112"。    

**示例 2：**
            **输入：** num = "32123"    **输出：** ""    **解释：** 不存在通过重组 "32123" 的数字可得、比 "32123" 还大的回文串。    

**示例 3：**
            **输入：** num = "45544554"    **输出：** "54455445"    **解释：** 下个比 "45544554" 还要大的回文串是 "54455445"。    

**提示：**

  * `1 <= num.length <= 105`
  * `num` 是回文串。


**Tags:** Two Pointers, String

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/next-palindrome-using-same-digits

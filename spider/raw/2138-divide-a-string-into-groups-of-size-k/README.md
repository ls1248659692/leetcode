# [Divide a String Into Groups of Size k][title]

## Description

字符串 `s` 可以按下述步骤划分为若干长度为 `k` 的组：

  * 第一组由字符串中的前 `k` 个字符组成，第二组由接下来的 `k` 个字符串组成，依此类推。每个字符都能够成为 **某一个** 组的一部分。
  * 对于最后一组，如果字符串剩下的字符 **不足** `k` 个，需使用字符 `fill` 来补全这一组字符。

注意，在去除最后一个组的填充字符 `fill`（如果存在的话）并按顺序连接所有的组后，所得到的字符串应该是 `s` 。

给你一个字符串 `s` ，以及每组的长度 `k` 和一个用于填充的字符 `fill` ，按上述步骤处理之后，返回一个字符串数组，该数组表示 `s` 分组后
**每个组的组成情况** 。



**示例 1：**
            **输入：** s = "abcdefghi", k = 3, fill = "x"    **输出：** ["abc","def","ghi"]    **解释：**    前 3 个字符是 "abc" ，形成第一组。    接下来 3 个字符是 "def" ，形成第二组。    最后 3 个字符是 "ghi" ，形成第三组。    由于所有组都可以由字符串中的字符完全填充，所以不需要使用填充字符。    因此，形成 3 组，分别是 "abc"、"def" 和 "ghi" 。    

**示例 2：**
            **输入：** s = "abcdefghij", k = 3, fill = "x"    **输出：** ["abc","def","ghi","jxx"]    **解释：**    与前一个例子类似，形成前三组 "abc"、"def" 和 "ghi" 。    对于最后一组，字符串中仅剩下字符 'j' 可以用。为了补全这一组，使用填充字符 'x' 两次。    因此，形成 4 组，分别是 "abc"、"def"、"ghi" 和 "jxx" 。    



**提示：**

  * `1 <= s.length <= 100`
  * `s` 仅由小写英文字母组成
  * `1 <= k <= 100`
  * `fill` 是一个小写英文字母


**Tags:** String, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s = s + fill*(k-len(s)%k) if len(s)%k != 0 else s
        li = []
        for i in range(0,len(s),k):
            li.append(s[i:i+k])
        return li
```

[title]: https://leetcode-cn.com/problems/divide-a-string-into-groups-of-size-k

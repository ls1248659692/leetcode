# [Guess the Word][title]

## Description

这是一个  ** _交互式问题_** 。

我们给出了一个由一些 **不同的** 单词组成的列表 `wordlist` ，对于每个 `wordlist[i]` 长度均为 `6`
，这个列表中的一个单词将被选作 `secret` 。

你可以调用 `Master.guess(word)` 来猜单词。你所猜的单词应当是存在于原列表并且由 `6` 个小写字母组成的类型 `string` 。

此函数将会返回一个 `integer` ，表示你的猜测与 **秘密单词**  `secret`
的准确匹配（值和位置同时匹配）的数目。此外，如果你的猜测不在给定的单词列表中，它将返回 `-1`。

对于每个测试用例，你有 `10` 次机会来猜出这个单词。当所有调用都结束时，如果您对 `Master.guess` 的调用在 `10`
次以内，并且至少有一次猜到 `secret` ，将判定为通过该用例。



**示例 1:**
            **输入:**  secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]    **输出:**  You guessed the secret word correctly.    **解释:**    master.guess("aaaaaa") 返回 -1, 因为 "aaaaaa" 不在 wordlist 中.    master.guess("acckzz") 返回 6, 因为 "acckzz" 就是 **秘密** ，6个字母完全匹配。    master.guess("ccbazz") 返回 3, 因为 "ccbazz" 有 3 个匹配项。    master.guess("eiowzz") 返回 2, 因为 "eiowzz" 有 2 个匹配项。    master.guess("abcczz") 返回 4, 因为 "abcczz" 有 4 个匹配项。    我们调用了 5 次master.guess，其中一次猜到了 **秘密** ，所以我们通过了这个测试用例。    

**  示例 2:**
            **输入:** secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10    **输出:** You guessed the secret word correctly.    



**提示:**

  * `1 <= wordlist.length <= 100`
  * `wordlist[i].length == 6`
  * `wordlist[i]` 只包含小写英文字母
  * `wordlist` 中所有字符串都 **不同**
  * `secret` 在 `wordlist` 中
  * `numguesses == 10`


**Tags:** Array, Math, String, Game Theory, Interactive

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/guess-the-word

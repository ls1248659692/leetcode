# [Number of Equivalent Domino Pairs][title]

## Description

给你一个由一些多米诺骨牌组成的列表 `dominoes`。

如果其中某一张多米诺骨牌可以通过旋转 `0` 度或 `180` 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，`dominoes[i] = [a, b]` 和 `dominoes[j] = [c, d]` 等价的前提是 `a==c` 且 `b==d`，或是
`a==d` 且 `b==c`。

在 `0 <= i < j < dominoes.length` 的前提下，找出满足 `dominoes[i]` 和 `dominoes[j]`
等价的骨牌对 `(i, j)` 的数量。



**示例：**
            **输入：** dominoes = [[1,2],[2,1],[3,4],[5,6]]    **输出：** 1    



**提示：**

  * `1 <= dominoes.length <= 40000`
  * `1 <= dominoes[i][j] <= 9`


**Tags:** Array, Hash Table, Counting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        cnt = 0
        dic = {}
        for a, b in dominoes:
            k = str(a) + str(b) if a > b else str(b) + str(a)
            dic[k] = dic.get(k, 0) + 1
        for k in dic:
            v = dic[k]
            if v > 1:
                cnt += (v * (v - 1)) // 2
        return cnt

```

[title]: https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs

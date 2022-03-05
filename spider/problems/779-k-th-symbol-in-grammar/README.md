# [K-th Symbol in Grammar][title]

## Description

在第一行我们写上一个 `0`。接下来的每一行，将前一行中的`0`替换为`01`，`1`替换为`10`。

给定行数 `N` 和序数 `K`，返回第 `N` 行中第 `K`个字符。（`K`从1开始）

  
**例子:**
            **输入:** N = 1, K = 1    **输出:** 0        **输入:** N = 2, K = 1    **输出:** 0        **输入:** N = 2, K = 2    **输出:** 1        **输入:** N = 4, K = 5    **输出:** 1        **解释:**    第一行: 0    第二行: 01    第三行: 0110    第四行: 01101001    

  
**注意：**

  1. `N` 的范围 `[1, 30]`.
  2. `K` 的范围 `[1, 2^(N-1)]`.


**Tags:** Bit Manipulation, Recursion, Math

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:return 0
        r = 2**(n-1)
        if k % 2:
            return self.kthGrammar(n-1,(k+1)/2)
        else:
            return abs(self.kthGrammar(n-1,k/2)-1)
```

[title]: https://leetcode-cn.com/problems/k-th-symbol-in-grammar

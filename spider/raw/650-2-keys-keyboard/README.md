# [2 Keys Keyboard][title]

## Description

最初记事本上只有一个字符 `'A'` 。你每次可以对这个记事本进行两种操作：

  * `Copy All`（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
  * `Paste`（粘贴）：粘贴 **上一次** 复制的字符。

给你一个数字 `n` ，你需要使用最少的操作次数，在记事本上输出 **恰好**  `n` 个 `'A'` 。返回能够打印出 `n` 个 `'A'`
的最少操作次数。



**示例 1：**
            **输入：** 3    **输出：** 3    **解释：**    最初, 只有一个字符 'A'。    第 1 步, 使用 **Copy All** 操作。    第 2 步, 使用 **Paste** 操作来获得 'AA'。    第 3 步, 使用 **Paste** 操作来获得 'AAA'。    

**示例 2：**
            **输入：** n = 1    **输出：** 0    



**提示：**

  * `1 <= n <= 1000`


**Tags:** Math, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def minSteps(self, n: int) -> int:
        def isprm(n=None):
            r=[]
            for i in range(2,10**3+1):
                isp=True
                for j in range(2,int(i**0.5)+1):
                    if i/j==i//j:
                        if n is not None and n==i:return j
                        isp=False
                        break
                if isp:r.append(i)
            return r if n is None else 1

        def ms(n):
            #print(isprm(None))
            if n==1: return 0
            elif n in isprm(None):return n
            else:
                j= isprm(n)
                print('gyz',j)
                return ms(j) +ms(n//j)
        return ms(n)
```

[title]: https://leetcode-cn.com/problems/2-keys-keyboard

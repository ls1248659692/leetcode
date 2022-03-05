# [Deep Dark Fraction][title]

## Description

有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/09/09/fraction_example_1.jpg)

连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。

输入的`cont`代表连分数的系数（`cont[0]`代表上图的`a0`，以此类推）。返回一个长度为2的数组`[n, m]`，使得连分数的值等于`n /
m`，且`n, m`最大公约数为1。

**示例 1：**
            **输入：** cont = [3, 2, 0, 2]    **输出：** [13, 4]    **解释：** 原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案。

**示例 2：**
            **输入：** cont = [0, 0, 3]    **输出：** [3, 1]    **解释：** 如果答案是整数，令分母为1即可。

**限制：**

  1. `cont[i] >= 0`
  2. `1 <= cont的长度 <= 10`
  3. `cont`最后一个元素不等于0
  4. 答案的`n, m`的取值都能被32位int整型存下（即不超过`2 ^ 31 - 1`）。


**Tags:** Array, Math, Number Theory, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        cont = cont[::-1]
        fz,fm =cont[0],1

        for i in range(1,len(cont)):
            fz,fm = fm,fz
            fz,fm = cont[i]*fm+fz,fm
        return [fz,fm]

```

[title]: https://leetcode-cn.com/problems/deep-dark-fraction

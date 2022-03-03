# [Complex Number Multiplication][title]

## Description

[复数](https://baike.baidu.com/item/%E5%A4%8D%E6%95%B0/254365?fr=aladdin)
可以用字符串表示，遵循 `" **实部** + **虚部** i"` 的形式，并满足下述条件：

  * `实部` 是一个整数，取值范围是 `[-100, 100]`
  * `虚部` 也是一个整数，取值范围是 `[-100, 100]`
  * `i2 == -1`

给你两个字符串表示的复数 `num1` 和 `num2` ，请你遵循复数表示形式，返回表示它们乘积的字符串。

**示例 1：**
            **输入：** num1 = "1+1i", num2 = "1+1i"    **输出：** "0+2i"    **解释：** (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。    

**示例 2：**
            **输入：** num1 = "1+-1i", num2 = "1+-1i"    **输出：** "0+-2i"    **解释：** (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。     

**提示：**

  * `num1` 和 `num2` 都是有效的复数表示。


**Tags:** Math, String, Simulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/complex-number-multiplication

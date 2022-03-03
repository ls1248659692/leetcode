# [Equal Rational Numbers][title]

## Description

给定两个字符串 `s` 和 `t` ，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 `true`
。字符串中可以使用括号来表示有理数的重复部分。

**有理数**  最多可以用三个部分来表示： _整数部分_  `<IntegerPart>`、 _小数非重复部分_
`<NonRepeatingPart>` 和 _小数重复部分_  `<(><RepeatingPart><)>`。数字可以用以下三种方法之一来表示：

  * `<IntegerPart>`     * 例： `0` ,`12` 和 `123` 
  * `<IntegerPart><.><NonRepeatingPart>`    * 例： `0.5 , ``1.` , `2.12` 和 `123.0001`
  * `<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>`     * 例： `0.1(6)` ， `1.(9)`， `123.00(1212)`

十进制展开的重复部分通常在一对圆括号内表示。例如：

  * `1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)`



**示例 1：**
            **输入：** s = "0.(52)", t = "0.5(25)"    **输出：** true    **解释：** 因为 "0.(52)" 代表 0.52525252...，而 "0.5(25)" 代表 0.52525252525.....，则这两个字符串表示相同的数字。    

**示例 2：**
            **输入：** s = "0.1666(6)", t = "0.166(66)"    **输出：** true    

**示例 3：**
            **输入：** s = "0.9(9)", t = "1."    **输出：** true    **解释：** "0.9(9)" 代表 0.999999999... 永远重复，等于 1 。[[有关说明，请参阅此链接](https://baike.baidu.com/item/0.999…/5615429?fr=aladdin)]    "1." 表示数字 1，其格式正确：(IntegerPart) = "1" 且 (NonRepeatingPart) = "" 。



**提示：**

  * 每个部分仅由数字组成。
  * 整数部分 `<IntegerPart>` 不会以零开头。（零本身除外）
  * `1 <= <IntegerPart>.length <= 4 `
  * `0 <= <NonRepeatingPart>.length <= 4 `
  * `1 <= <RepeatingPart>.length <= 4 `

​​​​​


**Tags:** Math, String

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/equal-rational-numbers

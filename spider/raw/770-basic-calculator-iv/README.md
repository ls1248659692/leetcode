# [Basic Calculator IV][title]

## Description

给定一个表达式如 `expression = "e + 8 - a + 5"` 和一个求值映射，如 `{"e": 1}`（给定的形式为 `evalvars
= ["e"]` 和 `evalints = [1]`），返回表示简化表达式的标记列表，例如 `["-1*a","14"]`

  * 表达式交替使用块和符号，每个块和符号之间有一个空格。
  * 块要么是括号中的表达式，要么是变量，要么是非负整数。
  * 变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 `"2x"` 或 `"-x"` 这样的前导系数或一元运算符 。

表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。

  * 例如，`expression = "1 + 2 * 3"` 的答案是 `["7"]`。

输出格式如下：

  * 对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。     * 例如，我们永远不会写像 `“b*a*c”` 这样的项，只写 `“a*b*c”`。
  * 项的次数等于被乘的自变量的数目，并计算重复项。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。     * 例如，`"a*a*b*c"` 的次数为 4。
  * 项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。
  * 格式良好的一个示例答案是 `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]` 。
  * 系数为 `0` 的项（包括常数项）不包括在内。     * 例如，`“0”` 的表达式输出为 `[]` 。



**示例 1：**
            **输入：** expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]    **输出：** ["-1*a","14"]    

**示例 2：**
            **输入：** expression = "e - 8 + temperature - pressure",    evalvars = ["e", "temperature"], evalints = [1, 12]    **输出：** ["-1*pressure","5"]    

**示例 3：**
            **输入：** expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []    **输出：** ["1*e*e","-64"]    



**提示：**

  * `1 <= expression.length <= 250`
  * `expression` 由小写英文字母，数字 `'+'`, `'-'`, `'*'`, `'('`, `')'`, `' '` 组成
  * `expression` 不包含任何前空格或后空格
  * `expression` 中的所有符号都用一个空格隔开
  * `0 <= evalvars.length <= 100`
  * `1 <= evalvars[i].length <= 20`
  * `evalvars[i]` 由小写英文字母组成
  * `evalints.length == evalvars.length`
  * `-100 <= evalints[i] <= 100`


**Tags:** Stack, Recursion, Hash Table, Math, String

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/basic-calculator-iv

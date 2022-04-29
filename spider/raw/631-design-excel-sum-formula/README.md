# [Design Excel Sum Formula][title]

## Description

你的任务是实现 Excel 的求和功能，具体的操作如下：

`Excel(int H, char W):` 这是一个构造函数，输入表明了 Excel 的高度和宽度。H 是一个正整数，范围从 1 到 26，代表高度。W
是一个字符，范围从 'A' 到 'Z'，宽度等于从 'A' 到 W 的字母个数。Excel 表格是一个高度 * 宽度的二维整数数组，数组中元素初始化为
0。第一行下标从 1 开始，第一列下标从 'A' 开始。

`void Set(int row, char column, int val):` 设置 `C(row, column)` 中的值为 val。

`int Get(int row, char column):` 返回 `C(row, column)` 中的值。

`int Sum(int row, char column, List of Strings : numbers):` 这个函数会将计算的结果放入
`C(row, column)` 中，计算的结果等于在 `numbers`
中代表的所有元素之和，这个函数同时也会将这个结果返回。求和公式会一直计算更新结果直到这个公式被其他的值或者公式覆盖。

`numbers` 是若干字符串的集合，每个字符串代表单个位置或一个区间。如果这个字符串表示单个位置，它的格式如下：`ColRow`，例如 "F7"
表示位置 (7, F) 。如果这个字符串表示一个区间，它的格式如下：`ColRow1:ColRow2`。区间就是左上角为 ColRow1 右下角为
ColRow2 的长方形。

**注意:** 你可以认为不会出现循环求和的定义，比如说：`mat[1]['A'] == sum(1, "B")` 和 `mat[1]['B'] ==
sum(1, "A")`.

**示例 1:**
            **输入:**    ["Excel", "set", "sum", "set", "get"]    [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]    **输出:**    [null, null, 4, null, 6]        **解释:**    Excel excel = new Excel(3, "C");     // 构造一个 3*3 的二维数组，初始化全是 0。     //   A B C     // 1 0 0 0     // 2 0 0 0     // 3 0 0 0    excel.set(1, "A", 2);     // 设置 C(1,"A") 为 2。     //   A B C     // 1 2 0 0     // 2 0 0 0     // 3 0 0 0    excel.sum(3, "C", ["A1", "A1:B2"]); // return 4     // 将 C(3,"C") 的值设为 C(1,"A") 单点以及左上角为 C(1,"A") 右下角为 C(2,"B") 的长方形两者之和。返回值 4。      // 1 2 0 0     // 2 0 0 0     // 3 0 0 4    excel.set(2, "B", 2);    // 将 C(2,"B") 设为 2。 注意 C(3, "C") 的值也同时改变。     //   A B C     // 1 2 0 0     // 2 0 2 0     // 3 0 0 6    excel.get(3, "C"); // 返回 6

**提示:**

  * `1 <= height <= 26`
  * `'A' <= width <= 'Z'`
  * `1 <= row <= height`
  * `'A' <= column <= width`
  * `-100 <= val <= 100`
  * `1 <= numbers.length <= 5`
  * `numbers[i]` 的格式为 `"ColRow"` 或 `"ColRow1:ColRow2"`.
  * `set`, `get`, and `sum` 操作数不超过 100 次


**Tags:** Graph, Design, Topological Sort

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/design-excel-sum-formula

# [Find Median Given Frequency of Numbers][title]

## Description

`Numbers` 表：
            +-------------+------+    | Column Name | Type |    +-------------+------+    | num         | int  |    | frequency   | int  |    +-------------+------+    num 是这张表的主键。这张表的每一行表示某个数字在该数据库中的出现频率。



[**中位数**](https://baike.baidu.com/item/%E4%B8%AD%E4%BD%8D%E6%95%B0/3087401)
是将数据样本中半数较高值和半数较低值分隔开的值。

编写一个 SQL 查询，解压 `Numbers` 表，报告数据库中所有数字的 **中位数** 。结果四舍五入至 **一位小数** 。

查询结果如下例所示。



**示例：**
            **输入：**     Numbers 表：    +-----+-----------+    | num | frequency |    +-----+-----------+    | 0   | 7         |    | 1   | 1         |    | 2   | 3         |    | 3   | 1         |    +-----+-----------+    **输出：**    +--------+    | median |    +--------+    | 0.0    |    +--------+    **解释：**    如果解压这个 Numbers 表，可以得到 [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3] ，所以中位数是 (0 + 0) / 2 = 0 。    


**Tags:** Database

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/find-median-given-frequency-of-numbers

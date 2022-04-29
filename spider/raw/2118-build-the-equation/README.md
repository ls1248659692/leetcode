# [Build the Equation][title]

## Description

Table: `Terms`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | power       | int  |    | factor      | int  |    +-------------+------+    power is the primary key column for this table.    Each row of this table contains information about one term of the equation.    power is an integer in the range [0, 100].    factor is an integer in the range [-100, 100] and cannot be zero.    



You have a very powerful program that can solve any equation of one variable
in the world. The equation passed to the program must be formatted as follows:

  * The left-hand side (LHS) should contain all the terms.
  * The right-hand side (RHS) should be zero.
  * Each term of the LHS should follow the format `"<sign><fact>X^<pow>"` where:     * `<sign>` is either `"+"` or `"-"`.    * `<fact>` is the **absolute value** of the `factor`.    * `<pow>` is the value of the `power`.
  * If the power is `1`, do not add `"^<pow>"`.     * For example, if `power = 1` and `factor = 3`, the term will be `"+3X"`.
  * If the power is `0`, add neither `"X"` nor `"^<pow>"`.     * For example, if `power = 0` and `factor = -3`, the term will be `"-3"`.
  * The powers in the LHS should be sorted in **descending order**.

Write an SQL query to build the equation.

The query result format is in the following example.



**Example 1:**
            Input:     Terms table:    +-------+--------+    | power | factor |    +-------+--------+    | 2     | 1      |    | 1     | -4     |    | 0     | 2      |    +-------+--------+    Output:     +--------------+    | equation     |    +--------------+    | +1X^2-4X+2=0 |    +--------------+    

**Example 2:**
            Input:     Terms table:    +-------+--------+    | power | factor |    +-------+--------+    | 4     | -4     |    | 2     | 1      |    | 1     | -1     |    +-------+--------+    Output:     +-----------------+    | equation        |    +-----------------+    | -4X^4+1X^2-1X=0 |    +-----------------+    



**Follow up:** What will be changed in your solution if the power is not a
primary key but each power should be unique in the answer?


**Tags:** Database

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/build-the-equation

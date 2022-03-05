# [Sales Person][title]

## Description

表: `SalesPerson`
            +-----------------+---------+    | Column Name     | Type    |    +-----------------+---------+    | sales_id        | int     |    | name            | varchar |    | salary          | int     |    | commission_rate | int     |    | hire_date       | date    |    +-----------------+---------+    Sales_id是该表的主键列。    该表的每一行都显示了销售人员的姓名和ID，以及他们的工资、佣金率和雇佣日期。    



表: `Company`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | com_id      | int     |    | name        | varchar |    | city        | varchar |    +-------------+---------+    Com_id是该表的主键列。    该表的每一行都表示公司的名称和ID，以及公司所在的城市。    



表: `Orders`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | order_id    | int  |    | order_date  | date |    | com_id      | int  |    | sales_id    | int  |    | amount      | int  |    +-------------+------+    Order_id是该表的主键列。    com_id是Company表中com_id的外键。    sales_id是来自销售员表com_id的外键。    该表的每一行包含一个订单的信息。这包括公司的ID、销售人员的ID、订单日期和支付的金额。    



编写一个SQL查询，报告没有任何与名为 **“RED”** 的公司相关的订单的所有销售人员的姓名。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。



**示例 1:**
            **输入:**     SalesPerson 表:    +----------+------+--------+-----------------+------------+    | sales_id | name | salary | commission_rate | hire_date  |    +----------+------+--------+-----------------+------------+    | 1        | John | 100000 | 6               | 4/1/2006   |    | 2        | Amy  | 12000  | 5               | 5/1/2010   |    | 3        | Mark | 65000  | 12              | 12/25/2008 |    | 4        | Pam  | 25000  | 25              | 1/1/2005   |    | 5        | Alex | 5000   | 10              | 2/3/2007   |    +----------+------+--------+-----------------+------------+    Company 表:    +--------+--------+----------+    | com_id | name   | city     |    +--------+--------+----------+    | 1      | RED    | Boston   |    | 2      | ORANGE | New York |    | 3      | YELLOW | Boston   |    | 4      | GREEN  | Austin   |    +--------+--------+----------+    Orders 表:    +----------+------------+--------+----------+--------+    | order_id | order_date | com_id | sales_id | amount |    +----------+------------+--------+----------+--------+    | 1        | 1/1/2014   | 3      | 4        | 10000  |    | 2        | 2/1/2014   | 4      | 5        | 5000   |    | 3        | 3/1/2014   | 1      | 1        | 50000  |    | 4        | 4/1/2014   | 1      | 4        | 25000  |    +----------+------------+--------+----------+--------+    **输出:**     +------+    | name |    +------+    | Amy  |    | Mark |    | Alex |    +------+    **解释:**    根据表 orders 中的订单 '3' 和 '4' ，容易看出只有 'John' 和 'Pam' 两个销售员曾经向公司 'RED' 销售过。    所以我们需要输出表 salesperson 中所有其他人的名字。


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/sales-person

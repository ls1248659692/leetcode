# [Count Salary Categories][title]

## Description

表: `Accounts`
            +-------------+------+    | 列名        | 类型  |    +-------------+------+    | account_id  | int  |    | income      | int  |    +-------------+------+    account_id 是这个表的主键。    每一行都包含一个银行帐户的月收入的信息。    

写出一个 SQL 查询，来报告每个工资类别的银行账户数量。 工资类别如下：

  * “低薪”：所有工资严格低于20000美元。
  * “中等薪水”：包含范围内的所有工资 [$20000, $50000]。
  * “高薪”：所有工资严格大于50000美元。

结果表必须包含所有三个类别。 如果某个类别中没有帐户，则报告 0。

按任意顺序返回结果表。

查询结果格式如下示例：
            Accounts 表:    +------------+--------+    | account_id | income |    +------------+--------+    | 3          | 108939 |    | 2          | 12747  |    | 8          | 87709  |    | 6          | 91796  |    +------------+--------+        Result 表:    +----------------+----------------+    | category       | accounts_count |    +----------------+----------------+    | Low Salary     | 1              |    | Average Salary | 0              |    | High Salary    | 3              |    +----------------+----------------+        低薪: 数量为 2.    中等薪水: 没有.    高薪: 有三个账户，他们是 3, 6和 8.    


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/count-salary-categories

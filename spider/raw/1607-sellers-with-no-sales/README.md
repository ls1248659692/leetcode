# [Sellers With No Sales][title]

## Description

表: `Customer`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | customer_id   | int     |    | customer_name | varchar |    +---------------+---------+    customer_id 是该表主键.    该表的每行包含网上商城的每一位顾客的信息.    



表: `Orders`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | order_id      | int     |    | sale_date     | date    |    | order_cost    | int     |    | customer_id   | int     |    | seller_id     | int     |    +---------------+---------+    order_id 是该表主键.    该表的每行包含网上商城的所有订单的信息.    sale_date 是顾客customer_id和卖家seller_id之间交易的日期.    



表: `Seller`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | seller_id     | int     |    | seller_name   | varchar |    +---------------+---------+    seller_id 是该表主键.    该表的每行包含每一位卖家的信息.    



写一个SQL语句, 报告所有在2020年度没有任何卖出的卖家的名字.

返回结果按照 `seller_name`  **升序排列**.

查询结果格式如下例所示.



**示例 1:**
            **输入：**    Customer 表:    +--------------+---------------+    | customer_id  | customer_name |    +--------------+---------------+    | 101          | Alice         |    | 102          | Bob           |    | 103          | Charlie       |    +--------------+---------------+    Orders 表:    +-------------+------------+--------------+-------------+-------------+    | order_id    | sale_date  | order_cost   | customer_id | seller_id   |    +-------------+------------+--------------+-------------+-------------+    | 1           | 2020-03-01 | 1500         | 101         | 1           |    | 2           | 2020-05-25 | 2400         | 102         | 2           |    | 3           | 2019-05-25 | 800          | 101         | 3           |    | 4           | 2020-09-13 | 1000         | 103         | 2           |    | 5           | 2019-02-11 | 700          | 101         | 2           |    +-------------+------------+--------------+-------------+-------------+    Seller 表:    +-------------+-------------+    | seller_id   | seller_name |    +-------------+-------------+    | 1           | Daniel      |    | 2           | Elizabeth   |    | 3           | Frank       |    +-------------+-------------+    **输出：**    +-------------+    | seller_name |    +-------------+    | Frank       |    +-------------+    **解释：**    Daniel在2020年3月卖出1次.    Elizabeth在2020年卖出2次, 在2019年卖出1次.    Frank在2019年卖出1次, 在2020年没有卖出.


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/sellers-with-no-sales

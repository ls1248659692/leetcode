# [The Most Frequently Ordered Products for Each Customer][title]

## Description

表：`Customers`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | customer_id   | int     |    | name          | varchar |    +---------------+---------+    customer_id 是该表主键    该表包含所有顾客的信息    

表：`Orders`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | order_id      | int     |    | order_date    | date    |    | customer_id   | int     |    | product_id    | int     |    +---------------+---------+    order_id 是该表主键    该表包含顾客 customer_id 的订单信息    没有顾客会在一天内订购相同的商品 **多于一次**

表：`Products`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | product_id    | int     |    | product_name  | varchar |    | price         | int     |    +---------------+---------+    product_id 是该表主键    该表包含了所有商品的信息    

写一个 SQL 语句，找到每一个顾客最经常订购的商品。

结果表单应该有每一位至少下过一次单的顾客 `customer_id` , 他最经常订购的商品的 `product_id` 和 `product_name`。

返回结果 **没有顺序要求** 。

查询结果格式如下例所示：
            Customers    +-------------+-------+    | customer_id | name  |    +-------------+-------+    | 1           | Alice |    | 2           | Bob   |    | 3           | Tom   |    | 4           | Jerry |    | 5           | John  |    +-------------+-------+        Orders    +----------+------------+-------------+------------+    | order_id | order_date | customer_id | product_id |    +----------+------------+-------------+------------+    | 1        | 2020-07-31 | 1           | 1          |    | 2        | 2020-07-30 | 2           | 2          |    | 3        | 2020-08-29 | 3           | 3          |    | 4        | 2020-07-29 | 4           | 1          |    | 5        | 2020-06-10 | 1           | 2          |    | 6        | 2020-08-01 | 2           | 1          |    | 7        | 2020-08-01 | 3           | 3          |    | 8        | 2020-08-03 | 1           | 2          |    | 9        | 2020-08-07 | 2           | 3          |    | 10       | 2020-07-15 | 1           | 2          |    +----------+------------+-------------+------------+        Products    +------------+--------------+-------+    | product_id | product_name | price |    +------------+--------------+-------+    | 1          | keyboard     | 120   |    | 2          | mouse        | 80    |    | 3          | screen       | 600   |    | 4          | hard disk    | 450   |    +------------+--------------+-------+    Result 表：    +-------------+------------+--------------+    | customer_id | product_id | product_name |    +-------------+------------+--------------+    | 1           | 2          | mouse        |    | 2           | 1          | keyboard     |    | 2           | 2          | mouse        |    | 2           | 3          | screen       |    | 3           | 3          | screen       |    | 4           | 1          | keyboard     |    +-------------+------------+--------------+        Alice (customer 1) 三次订购鼠标, 一次订购键盘, 所以鼠标是 Alice 最经常订购的商品.    Bob (customer 2) 一次订购键盘, 一次订购鼠标, 一次订购显示器, 所以这些都是 Bob 最经常订购的商品.    Tom (customer 3) 只两次订购显示器, 所以显示器是 Tom 最经常订购的商品.    Jerry (customer 4) 只一次订购键盘, 所以键盘是 Jerry 最经常订购的商品.    John (customer 5) 没有订购过商品, 所以我们并没有把 John 包含在结果表中.    


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/the-most-frequently-ordered-products-for-each-customer

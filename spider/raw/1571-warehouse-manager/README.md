# [Warehouse Manager][title]

## Description

表: `Warehouse`
            +--------------+---------+    | Column Name  | Type    |    +--------------+---------+    | name         | varchar |    | product_id   | int     |    | units        | int     |    +--------------+---------+    (name, product_id) 是该表主键.    该表的行包含了每个仓库的所有商品信息.    



表: `Products`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | product_id    | int     |    | product_name  | varchar |    | Width         | int     |    | Length        | int     |    | Height        | int     |    +---------------+---------+    product_id 是该表主键.    该表的行包含了每件商品以英尺为单位的尺寸(宽度, 长度和高度)信息.    



写一个 SQL 查询来报告, 每个仓库的存货量是多少立方英尺.

返回结果没有顺序要求.

查询结果如下例所示.



**示例 1:**
            **输入：**    Warehouse 表:    +------------+--------------+-------------+    | name       | product_id   | units       |    +------------+--------------+-------------+    | LCHouse1   | 1            | 1           |    | LCHouse1   | 2            | 10          |    | LCHouse1   | 3            | 5           |    | LCHouse2   | 1            | 2           |    | LCHouse2   | 2            | 2           |    | LCHouse3   | 4            | 1           |    +------------+--------------+-------------+    Products 表:    +------------+--------------+------------+----------+-----------+    | product_id | product_name | Width      | Length   | Height    |    +------------+--------------+------------+----------+-----------+    | 1          | LC-TV        | 5          | 50       | 40        |    | 2          | LC-KeyChain  | 5          | 5        | 5         |    | 3          | LC-Phone     | 2          | 10       | 10        |    | 4          | LC-T-Shirt   | 4          | 10       | 20        |    +------------+--------------+------------+----------+-----------+    **输出：**    +----------------+------------+    | WAREHOUSE_NAME | VOLUME     |     +----------------+------------+    | LCHouse1       | 12250      |     | LCHouse2       | 20250      |    | LCHouse3       | 800        |    +----------------+------------+    **解释：**    Id为1的商品(LC-TV)的存货量为 5x50x40 = 10000    Id为2的商品(LC-KeyChain)的存货量为 5x5x5 = 125     Id为3的商品(LC-Phone)的存货量为 2x10x10 = 200    Id为4的商品(LC-T-Shirt)的存货量为 4x10x20 = 800    仓库LCHouse1: 1个单位的LC-TV + 10个单位的LC-KeyChain + 5个单位的LC-Phone.              总存货量为: 1*10000 + 10*125  + 5*200 = 12250 立方英尺    仓库LCHouse2: 2个单位的LC-TV + 2个单位的LC-KeyChain.              总存货量为: 2*10000 + 2*125 = 20250 立方英尺    仓库LCHouse3: 1个单位的LC-T-Shirt.              总存货量为: 1*800 = 800 立方英尺.


**Tags:** Database

**Difficulty:** Easy

## 思路

``` mysql
# Write your MySQL query statement below
SELECT name AS warehouse_name, SUM(Width * Length * Height * units) AS volume
FROM Warehouse
         LEFT JOIN Products ON Warehouse.product_id = Products.product_id
GROUP BY name;

```

[title]: https://leetcode-cn.com/problems/warehouse-manager

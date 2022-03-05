# [Find Customer Referee][title]

## Description

给定表 `customer` ，里面保存了所有客户信息和他们的推荐人。
            +------+------+-----------+    | id   | name | referee_id|    +------+------+-----------+    |    1 | Will |      NULL |    |    2 | Jane |      NULL |    |    3 | Alex |         2 |    |    4 | Bill |      NULL |    |    5 | Zack |         1 |    |    6 | Mark |         2 |    +------+------+-----------+    

写一个查询语句，返回一个客户列表，列表中客户的推荐人的编号都 **不是** 2。

对于上面的示例数据，结果为：
            +------+    | name |    +------+    | Will |    | Jane |    | Bill |    | Zack |    +------+    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/find-customer-referee

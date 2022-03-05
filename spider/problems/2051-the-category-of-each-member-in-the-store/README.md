# [The Category of Each Member in the Store][title]

## Description

Table: `Members`
            +-------------+---------+    | Column Name | Type    |    +-------------+---------+    | member_id   | int     |    | name        | varchar |    +-------------+---------+    member_id is the primary key column for this table.    Each row of this table indicates the name and the ID of a member.    



Table: `Visits`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | visit_id    | int  |    | member_id   | int  |    | visit_date  | date |    +-------------+------+    visit_id is the primary key column for this table.    member_id is a foreign key to member_id from the Members table.    Each row of this table contains information about the date of a visit to the store and the member who visited it.    



Table: `Purchases`
            +----------------+------+    | Column Name    | Type |    +----------------+------+    | visit_id       | int  |    | charged_amount | int  |    +----------------+------+    visit_id is the primary key column for this table.    visit_id is a foreign key to visit_id from the Visits table.    Each row of this table contains information about the amount charged in a visit to the store.    



A store wants to categorize its members. There are three tiers:

  * **" Diamond"**: if the conversion rate is **greater than or equal to** `80`.
  * **" Gold"**: if the conversion rate is **greater than or equal to** `50` and less than `80`.
  * **" Silver"**: if the conversion rate is **less than** `50`.
  * **" Bronze"**: if the member never visited the store.

The **conversion rate** of a member is `(100 * total number of purchases for
the member) / total number of visits for the member`.

Write an SQL query to report the id, the name, and the category of each
member.

Return the result table in **any order**.

The query result format is in the following example.



**Example 1:**
            Input:     Members table:    +-----------+---------+    | member_id | name    |    +-----------+---------+    | 9         | Alice   |    | 11        | Bob     |    | 3         | Winston |    | 8         | Hercy   |    | 1         | Narihan |    +-----------+---------+    Visits table:    +----------+-----------+------------+    | visit_id | member_id | visit_date |    +----------+-----------+------------+    | 22       | 11        | 2021-10-28 |    | 16       | 11        | 2021-01-12 |    | 18       | 9         | 2021-12-10 |    | 19       | 3         | 2021-10-19 |    | 12       | 11        | 2021-03-01 |    | 17       | 8         | 2021-05-07 |    | 21       | 9         | 2021-05-12 |    +----------+-----------+------------+    Purchases table:    +----------+----------------+    | visit_id | charged_amount |    +----------+----------------+    | 12       | 2000           |    | 18       | 9000           |    | 17       | 7000           |    +----------+----------------+    Output:     +-----------+---------+----------+    | member_id | name    | category |    +-----------+---------+----------+    | 1         | Narihan | Bronze   |    | 3         | Winston | Silver   |    | 8         | Hercy   | Diamond  |    | 9         | Alice   | Gold     |    | 11        | Bob     | Silver   |    +-----------+---------+----------+    Explanation:     - User Narihan with id = 1 did not make any visits to the store. She gets a Bronze category.    - User Winston with id = 3 visited the store one time and did not purchase anything. The conversion rate = (100 * 0) / 1 = 0. He gets a Silver category.    - User Hercy with id = 8 visited the store one time and purchased one time. The conversion rate = (100 * 1) / 1 = 1. He gets a Diamond category.    - User Alice with id = 9 visited the store two times and purchased one time. The conversion rate = (100 * 1) / 2 = 50. She gets a Gold category.    - User Bob with id = 11 visited the store three times and purchased one time. The conversion rate = (100 * 1) / 3 = 33.33. He gets a Silver category.    


**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/the-category-of-each-member-in-the-store

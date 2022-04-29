# [Patients With a Condition][title]

## Description

患者信息表： `Patients`
            +--------------+---------+    | Column Name  | Type    |    +--------------+---------+    | patient_id   | int     |    | patient_name | varchar |    | conditions   | varchar |    +--------------+---------+    patient_id （患者 ID）是该表的主键。    'conditions' （疾病）包含 0 个或以上的疾病代码，以空格分隔。    这个表包含医院中患者的信息。



写一条 SQL 语句，查询患有 I 类糖尿病的患者 ID
（patient_id）、患者姓名（patient_name）以及其患有的所有疾病代码（conditions）。I 类糖尿病的代码总是包含前缀
`DIAB1` 。

按任意顺序返回结果表。

查询结果格式如下示例所示：


            Patients    +------------+--------------+--------------+    | patient_id | patient_name | conditions   |    +------------+--------------+--------------+    | 1          | Daniel       | YFEV COUGH   |    | 2          | Alice        |              |    | 3          | Bob          | DIAB100 MYOP |    | 4          | George       | ACNE DIAB100 |    | 5          | Alain        | DIAB201      |    +------------+--------------+--------------+        结果表：    +------------+--------------+--------------+    | patient_id | patient_name | conditions   |    +------------+--------------+--------------+    | 3          | Bob          | DIAB100 MYOP |    | 4          | George       | ACNE DIAB100 |     +------------+--------------+--------------+    Bob 和 George 都患有代码以 DIAB1 开头的疾病。    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/patients-with-a-condition

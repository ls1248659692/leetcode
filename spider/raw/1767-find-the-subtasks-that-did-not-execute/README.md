# [Find the Subtasks That Did Not Execute][title]

## Description

表：`Tasks`
            +----------------+---------+    | Column Name    | Type    |    +----------------+---------+    | task_id        | int     |    | subtasks_count | int     |    +----------------+---------+    task_id 是这个表的主键。    task_id 表示的为主任务的id,每一个task_id被分为了多个子任务(subtasks)，subtasks_count表示为子任务的个数（n），它的值表示了子任务的索引从1到n。    本表保证2 <=subtasks_count<= 20。    



表： `Executed`
            +---------------+---------+    | Column Name   | Type    |    +---------------+---------+    | task_id       | int     |    | subtask_id    | int     |    +---------------+---------+    (task_id, subtask_id) 是这个表的主键。    每一行表示标记为task_id的主任务与标记为subtask_id的子任务被成功执行。    本表 **保证** ，对于每一个task_id，subtask_id <= subtasks_count。    



请试写一个SQL查询语句报告没有被执行的（主任务，子任务）对，即没有被执行的（task_id, subtask_id）。

以 **任何顺序** 返回即可。

查询结果格式如下。



**示例 1：**
            **输入：** Tasks 表:    +---------+----------------+    | task_id | subtasks_count |    +---------+----------------+    | 1       | 3              |    | 2       | 2              |    | 3       | 4              |    +---------+----------------+    Executed 表:    +---------+------------+    | task_id | subtask_id |    +---------+------------+    | 1       | 2          |    | 3       | 1          |    | 3       | 2          |    | 3       | 3          |    | 3       | 4          |    +---------+------------+    **输出：**    +---------+------------+    | task_id | subtask_id |    +---------+------------+    | 1       | 1          |    | 1       | 3          |    | 2       | 1          |    | 2       | 2          |    +---------+------------+    **解释：**    Task 1 被分成了 3 subtasks (1, 2, 3)。只有 subtask 2 被成功执行, 所以我们返回 (1, 1) 和 (1, 3) 这两个主任务子任务对。    Task 2 被分成了 2 subtasks (1, 2)。没有一个subtask被成功执行, 因此我们返回(2, 1)和(2, 2)。    Task 3 被分成了 4 subtasks (1, 2, 3, 4)。所有的subtask都被成功执行，因此对于Task 3,我们不返回任何值。


**Tags:** Database

**Difficulty:** Hard

## 思路

``` mysql
# Write your MySQL query statement below

WITH RECURSIVE seq AS (SELECT 1 AS value UNION ALL SELECT value + 1 FROM seq LIMIT 20)
    SELECT t.task_id, seq.value as subtask_id
    FROM Tasks t
    LEFT JOIN seq ON t.subtasks_count >= seq.value
    LEFT JOIN Executed e ON t.task_id = e.task_id AND seq.value = e.subtask_id
    WHERE e.subtask_id IS NULL
```

[title]: https://leetcode-cn.com/problems/find-the-subtasks-that-did-not-execute

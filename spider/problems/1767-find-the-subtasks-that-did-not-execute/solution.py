# Write your MySQL query statement below

WITH RECURSIVE seq AS (SELECT 1 AS value UNION ALL SELECT value + 1 FROM seq LIMIT 20)
    SELECT t.task_id, seq.value as subtask_id
    FROM Tasks t
    LEFT JOIN seq ON t.subtasks_count >= seq.value
    LEFT JOIN Executed e ON t.task_id = e.task_id AND seq.value = e.subtask_id
    WHERE e.subtask_id IS NULL
# Write your MySQL query statement below
SELECT request_at AS Day, ROUND(COUNT(CASE WHEN status != 'completed' THEN 1 END)/COUNT(*), 2) AS 'Cancellation Rate'
FROM (SELECT status, request_at
FROM Trips t
JOIN Users u1 ON t.client_id = u1.users_id AND u1.banned = 'No'
JOIN Users u2 ON t.driver_id = u2.users_id AND u2.banned = 'No'
WHERE request_at >= '2013-10-01' AND request_at <= '2013-10-03') f
GROUP BY request_at
# Write your MySQL query statement below
select Name as Customers from Customers where id not in (select customerid from orders)
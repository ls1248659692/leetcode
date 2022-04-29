# Write your MySQL query statement below

SELECT DISTINCT d.id, m1.revenue AS Jan_Revenue, m2.revenue AS Feb_Revenue, m3.revenue AS Mar_Revenue, m4.revenue AS Apr_Revenue, m5.revenue AS May_Revenue, m6.revenue AS Jun_Revenue, m7.revenue AS Jul_Revenue, m8.revenue AS Aug_Revenue, m9.revenue AS Sep_Revenue, m10.revenue AS Oct_Revenue, m11.revenue AS Nov_Revenue, m12.revenue AS Dec_Revenue
FROM Department d
LEFT JOIN Department m1 ON m1.id = d.id AND m1.month = 'Jan'
LEFT JOIN Department m2 ON m2.id = d.id AND m2.month = 'Feb'
LEFT JOIN Department m3 ON m3.id = d.id AND m3.month = 'Mar'
LEFT JOIN Department m4 ON m4.id = d.id AND m4.month = 'Apr'
LEFT JOIN Department m5 ON m5.id = d.id AND m5.month = 'May'
LEFT JOIN Department m6 ON m6.id = d.id AND m6.month = 'Jun'
LEFT JOIN Department m7 ON m7.id = d.id AND m7.month = 'Jul'
LEFT JOIN Department m8 ON m8.id = d.id AND m8.month = 'Aug'
LEFT JOIN Department m9 ON m9.id = d.id AND m9.month = 'Sep'
LEFT JOIN Department m10 ON m10.id = d.id AND m10.month = 'Oct'
LEFT JOIN Department m11 ON m11.id = d.id AND m11.month = 'Nov'
LEFT JOIN Department m12 ON m12.id = d.id AND m12.month = 'Dec'
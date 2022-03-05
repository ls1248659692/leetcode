# [Ad-Free Sessions][title]

## Description

Table: `Playback`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | session_id  | int  |    | customer_id | int  |    | start_time  | int  |    | end_time    | int  |    +-------------+------+    该表主键为：session_id （剧集id）    customer_id 是观看该剧集的观众id    剧集播放时间包含start_time（开始时间） 及 end_time（结束时间）    可以保证的是，start_time（开始时间）<= end_time（结束时间），一个观众观看的两个剧集的时间不会出现重叠。

Table: `Ads`
            +-------------+------+    | Column Name | Type |    +-------------+------+    | ad_id       | int  |    | customer_id | int  |    | timestamp   | int  |    +-------------+------+    该表的主键为：ad_id（广告id）    customer_id 为 观看广告的用户id    timestamp 表示广告出现的时间点    

请查出，所有没有广告出现过的剧集。

如果观众观看了剧集，并且剧集里出现了广告，就一定会有观众观看广告的记录。

返回结果没有顺序要求。

示例：
            Playback table:    +------------+-------------+------------+----------+    | session_id | customer_id | start_time | end_time |    +------------+-------------+------------+----------+    | 1          | 1           | 1          | 5        |    | 2          | 1           | 15         | 23       |    | 3          | 2           | 10         | 12       |    | 4          | 2           | 17         | 28       |    | 5          | 2           | 2          | 8        |    +------------+-------------+------------+----------+        Ads table:    +-------+-------------+-----------+    | ad_id | customer_id | timestamp |    +-------+-------------+-----------+    | 1     | 1           | 5         |    | 2     | 2           | 17        |    | 3     | 2           | 20        |    +-------+-------------+-----------+        Result table:    +------------+    | session_id |    +------------+    | 2          |    | 3          |    | 5          |    +------------+    广告1出现在了剧集1的时间段，被观众1看到了。    广告2出现在了剧集4的时间段，被观众2看到了。    广告3出现在了剧集4的时间段，被观众2看到了。    我们可以得出结论，剧集1 、4 内，起码有1处广告。 剧集2 、3 、5 没有广告。


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/ad-free-sessions

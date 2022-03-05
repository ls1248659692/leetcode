# [Invalid Tweets][title]

## Description

表：`Tweets`
            +----------------+---------+    | Column Name    | Type    |    +----------------+---------+    | tweet_id       | int     |    | content        | varchar |    +----------------+---------+    tweet_id 是这个表的主键。    这个表包含某社交媒体 App 中所有的推文。

写一条 SQL 语句，查询所有无效推文的编号（ID）。当推文内容中的字符数 **严格大于** `15` 时，该推文是无效的。

以 **任意顺序** 返回结果表。

查询结果格式如下示例所示：
            Tweets 表：    +----------+----------------------------------+    | tweet_id | content                          |    +----------+----------------------------------+    | 1        | Vote for Biden                   |    | 2        | Let us make America great again! |    +----------+----------------------------------+        结果表：    +----------+    | tweet_id |    +----------+    | 2        |    +----------+    推文 1 的长度 length = 14。该推文是有效的。    推文 2 的长度 length = 32。该推文是无效的。    


**Tags:** Database

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/invalid-tweets

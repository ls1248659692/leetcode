# [Second Degree Follower][title]

## Description

在 facebook 中，表 `follow` 会有 2 个字段： **followee** , **follower**  ，分别表示被关注者和关注者。

请写一个 sql 查询语句，对每一个关注者，查询关注他的关注者的数目。

比方说：
            +-------------+------------+    | followee    | follower   |    +-------------+------------+    |     A       |     B      |    |     B       |     C      |    |     B       |     D      |    |     D       |     E      |    +-------------+------------+    

应该输出：
            +-------------+------------+    | follower    | num        |    +-------------+------------+    |     B       |  2         |    |     D       |  1         |    +-------------+------------+    

**解释：**

B 和 D 都在在  **follower**  字段中出现，作为被关注者，B 被 C 和 D 关注，D 被 E 关注。A 不在 **follower**
字段内，所以A不在输出列表中。



**注意：**

  * 被关注者永远不会被他 / 她自己关注。
  * 将结果按照字典序返回。




**Tags:** Database

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/second-degree-follower

# [Handshakes That Don't Cross][title]

## Description

**偶数**  个人站成一个圆，总人数为 `num_people` 。每个人与除自己外的一个人握手，所以总共会有 `num_people / 2` 次握手。

将握手的人之间连线，请你返回连线不会相交的握手方案数。

由于结果可能会很大，请你返回答案 **模**   **`10^9+7`**  后的结果。



**示例 1：**
            **输入：** num_people = 2    **输出：** 1    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/16/5125_example_2.png)
            **输入：** num_people = 4    **输出：** 2    **解释：** 总共有两种方案，第一种方案是 [(1,2),(3,4)] ，第二种方案是 [(2,3),(4,1)] 。    

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/11/16/5125_example_3.png)
            **输入：** num_people = 6    **输出：** 5    

**示例 4：**
            **输入：** num_people = 8    **输出：** 14    



**提示：**

  * `2 <= num_people <= 1000`
  * `num_people % 2 == 0`


**Tags:** Math, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/handshakes-that-dont-cross

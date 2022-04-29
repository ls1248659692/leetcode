# [Design Hit Counter][title]

## Description

设计一个敲击计数器，使它可以统计在过去 `5` 分钟内被敲击次数。（即过去 `300` 秒）

您的系统应该接受一个时间戳参数 `timestamp` (单位为 **秒**  )，并且您可以假定对系统的调用是按时间顺序进行的(即 `timestamp`
是单调递增的)。几次撞击可能同时发生。

实现 `HitCounter` 类:

  * `HitCounter()` 初始化命中计数器系统。
  * `void hit(int timestamp)` 记录在 `timestamp` (  **单位为秒**  )发生的一次命中。在同一个 `timestamp` 中可能会出现几个点击。
  * `int getHits(int timestamp)` 返回 `timestamp` 在过去 5 分钟内(即过去 `300` 秒)的命中次数。



**示例 1:**
            **输入：**    ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]    [[], [1], [2], [3], [4], [300], [300], [301]]    **输出：**    [null, null, null, null, 3, null, 4, 3]        **解释：**    HitCounter counter = new HitCounter();    counter.hit(1);// 在时刻 1 敲击一次。    counter.hit(2);// 在时刻 2 敲击一次。    counter.hit(3);// 在时刻 3 敲击一次。    counter.getHits(4);// 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。    counter.hit(300);// 在时刻 300 敲击一次。    counter.getHits(300); // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。    counter.getHits(301); // 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。    



**提示:**

  * `1 <= timestamp <= 2 * 109`
  * 所有对系统的调用都是按时间顺序进行的（即 `timestamp` 是单调递增的）
  * `hit` and `getHits `最多被调用 `300` 次



**进阶:**  如果每秒的敲击次数是一个很大的数字，你的计数器可以应对吗？


**Tags:** Design, Queue, Array, Hash Table, Binary Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/design-hit-counter

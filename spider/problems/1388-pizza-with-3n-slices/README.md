# [Pizza With 3n Slices][title]

## Description

给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：

  * 你挑选 **任意**  一块披萨。
  * Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
  * Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
  * 重复上述过程直到没有披萨剩下。

每一块披萨的大小按顺时针方向由循环数组 `slices` 表示。

请你返回你可以获得的披萨大小总和的最大值。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/03/21/sample_3_1723.png)
            **输入：** slices = [1,2,3,4,5,6]    **输出：** 10    **解释：** 选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/03/21/sample_4_1723.png)**
            **输入：** slices = [8,9,8,6,1,1]    **输出：** 16    **解释：** 两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。    

**示例 3：**
            **输入：** slices = [4,1,2,5,8,3,1,9,7]    **输出：** 21    

**示例 4：**
            **输入：** slices = [3,1,2]    **输出：** 3    



**提示：**

  * `1 <= slices.length <= 500`
  * `slices.length % 3 == 0`
  * `1 <= slices[i] <= 1000`


**Tags:** Greedy, Array, Dynamic Programming, Heap (Priority Queue)

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/pizza-with-3n-slices

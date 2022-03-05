# [Game of Nim][title]

## Description

Alice 和 Bob 交替进行一个游戏， **由 Alice 先手** 。

在游戏中，共有 `n` 堆石头。在每个玩家的回合中，玩家需要 **选择** 任一非空石头堆，从中移除任意 **非零**
数量的石头。如果不能移除任意的石头，就输掉游戏，同时另一人获胜。

给定一个整数数组 `piles` ，`piles[i]` 为 第 `i` 堆石头的数量，如果 Alice 能获胜返回 `true` _ _ ，反之返回
`false` _  。_

Alice 和 Bob 都会采取 **最优策略** 。



**示例 1：**
            **输入：** piles = [1]    **输出：** true    **解释：** 只有一种可能的情况：    - 第一回合，Alice 移除了第 1 堆中 1 块石头。piles = [0]。    - 第二回合，Bob 没有任何石头可以移除。Alice 获胜。    

**示例  2：**
            **输入：** piles = [1,1]    **输出：** false    **解释：** 可以证明，Bob一定能获胜。一种可能的情况：    - 第一回合，Alice 移除了第 1 堆中 1 块石头。 piles = [0,1]。    - 第二回合，Bob 移除了第 2 堆中 1 块石头。 piles = [0,0]。    - 第三回合，Alice 没有任何石头可以移除。Bob 获胜。    

**示例 3：**
            **输入：** piles = [1,2,3]    **输出：** false    **解释：** 可以证明，Bob一定能获胜。一种可能的情况：    - 第一回合，Alice 移除了第 3 堆中 3 块石头。 piles = [1,2,0]。    - 第二回合，Bob 移除了第 2 堆中 1 块石头。 piles = [1,1,0]。    - 第三回合，Alice 移除了第 1 堆中 1 块石头。piles = [0,1,0]。    - 第四回合，Bob 移除了第 2 堆中 1 块石头。 piles = [0,0,0]。    - 第三回合，Alice 没有任何石头可以移除。Bob 获胜。



**提示：**

  * `n == piles.length`
  * `1 <= n <= 7`
  * `1 <= piles[i] <= 7`



**进阶：** 你能想出一个  **线性时间  **的解决方案吗？虽然这一答案可能超出了面试所需的范围，但了解它可能会很有趣。


**Tags:** Bit Manipulation, Brainteaser, Array, Math, Dynamic Programming, Game Theory

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/game-of-nim

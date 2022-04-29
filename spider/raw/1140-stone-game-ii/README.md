# [Stone Game II][title]

## Description

爱丽丝和鲍勃继续他们的石子游戏。许多堆石子  **排成一行** ，每堆都有正整数颗石子 `piles[i]`。游戏以谁手中的石子最多来决出胜负。

爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，`M = 1`。

在每个玩家的回合中，该玩家可以拿走剩下的  **前**  `X` 堆的所有石子，其中 `1 <= X <= 2M`。然后，令 `M = max(M,
X)`。

游戏一直持续到所有石子都被拿走。

假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。



**示例 1：**
            **输入：** piles = [2,7,9,4,4]    **输出：** 10    **解释：** 如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。    

**示例 2:**
            **输入：** piles = [1,2,3,4,5,100]    **输出：** 104    



**提示：**

  * `1 <= piles.length <= 100`
  * `1 <= piles[i] <= 104`


**Tags:** Array, Math, Dynamic Programming, Game Theory

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/stone-game-ii

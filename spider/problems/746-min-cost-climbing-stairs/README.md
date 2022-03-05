# [Min Cost Climbing Stairs][title]

## Description

给你一个整数数组 `cost` ，其中 `cost[i]` 是从楼梯第 `i`
个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 `0` 或下标为 `1` 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。



**示例 1：**
            **输入：** cost = [10, _ **15**_ ,20]    **输出：** 15    **解释：** 你将从下标为 1 的台阶开始。    - 支付 15 ，向上爬两个台阶，到达楼梯顶部。    总花费为 15 。    

**示例 2：**
            **输入：** cost = [ _ **1**_ ,100, _ **1**_ ,1, _ **1**_ ,100, _ **1**_ , _ **1**_ ,100, _ **1**_ ]    **输出：** 6    **解释：** 你将从下标为 0 的台阶开始。    - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。    - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。    - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。    - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。    - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。    - 支付 1 ，向上爬一个台阶，到达楼梯顶部。    总花费为 6 。    



**提示：**

  * `2 <= cost.length <= 1000`
  * `0 <= cost[i] <= 999`


**Tags:** Array, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l,r=0,len(cost)
        @lru_cache
        def cst(l,m):
            if r-l in[1]: return cost[l] if m==1 else 0
            else:
                return  min(cst(l+1,1)if m!=1 else float('inf'),cst(l+1,0)+cost[l]) 
        return min(cst(1,1),cst(1,0)+cost[0] )
```

[title]: https://leetcode-cn.com/problems/min-cost-climbing-stairs

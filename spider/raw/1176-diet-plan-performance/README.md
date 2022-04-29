# [Diet Plan Performance][title]

## Description

你的好友是一位健身爱好者。前段日子，他给自己制定了一份健身计划。现在想请你帮他评估一下这份计划是否合理。

他会有一份计划消耗的卡路里表，其中 `calories[i]` 给出了你的这位好友在第 `i` 天需要消耗的卡路里总量。

为了更好地评估这份计划，对于卡路里表中的每一天，你都需要计算他 「这一天以及之后的连续几天」 （共 `k` 天）内消耗的总卡路里 _T：_

  * 如果 `T < lower`，那么这份计划相对糟糕，并失去 1 分； 
  * 如果 `T > upper`，那么这份计划相对优秀，并获得 1 分；
  * 否则，这份计划普普通通，分值不做变动。

请返回统计完所有 `calories.length` 天后得到的总分作为评估结果。

注意：总分可能是负数。



**示例 1：**
            **输入：** calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3    **输出：** 0    **解释：** calories[0], calories[1] < lower 而 calories[3], calories[4] > upper, 总分 = 0.

**示例 2：**
            **输入：** calories = [3,2], k = 2, lower = 0, upper = 1    **输出：** 1    **解释：** calories[0] + calories[1] > upper, 总分 = 1.    

**示例 3：**
            **输入：** calories = [6,5,0,0], k = 2, lower = 1, upper = 5    **输出：** 0    **解释：** calories[0] + calories[1] > upper, calories[2] + calories[3] < lower, 总分 = 0.    



**提示：**

  * `1 <= k <= calories.length <= 10^5`
  * `0 <= calories[i] <= 20000`
  * `0 <= lower <= upper`


**Tags:** Array, Sliding Window

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        window_sum = sum(calories[ :k]) 
        res = 0
        if window_sum < lower:
            res -= 1
        elif window_sum > upper:
            res += 1
        for R in range(k, n):      
            window_sum -= calories[R-k] 
            window_sum += calories[R]   
            if window_sum < lower:
                res -= 1
            elif window_sum > upper:
                res += 1
        return res

```

[title]: https://leetcode-cn.com/problems/diet-plan-performance

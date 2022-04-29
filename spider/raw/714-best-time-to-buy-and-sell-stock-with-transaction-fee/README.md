# [Best Time to Buy and Sell Stock with Transaction Fee][title]

## Description

给定一个整数数组 `prices`，其中 `prices[i]`表示第 `i` 天的股票价格 ；整数 `fee` 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

**注意：** 这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。



**示例 1：**
            **输入：** prices = [1, 3, 2, 8, 4, 9], fee = 2    **输出：** 8    **解释：** 能够达到的最大利润:      在此处买入 prices[0] = 1    在此处卖出 prices[3] = 8    在此处买入 prices[4] = 4    在此处卖出 prices[5] = 9    总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8

**示例 2：**
            **输入：** prices = [1,3,7,5,10,3], fee = 3    **输出：** 6    



**提示：**

  * `1 <= prices.length <= 5 * 104`
  * `1 <= prices[i] < 5 * 104`
  * `0 <= fee < 5 * 104`


**Tags:** Greedy, Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def v2(pr):
            dp = [[0,pr[0],None] for _ in range(len(pr))] #prof min sellpr(Noneè¡¨ç¤ºæ°çäº¤æå¨æ)   
            for i in range(1,len(pr)):
                #print(dp[:i])
                lastDp= dp[i-1][:]
                if lastDp[2] is not None:
                    if lastDp[2]<pr[i]:
                        lastDp[0],lastDp[2]=lastDp[0]+pr[i]-lastDp[2],pr[i]
                    elif lastDp[2]-fee<pr[i]:
                        lastDp[1]=pr[i]
                    else:
                        lastDp[1], lastDp[2]=pr[i],None
                else:
                    if lastDp[1]<pr[i]-fee:
                        lastDp[0],lastDp[2]=lastDp[0]+pr[i]-lastDp[1]-fee,pr[i]
                    elif lastDp[1]>pr[i]:
                        lastDp[1]=pr[i]
                dp[i][0],dp[i][1],dp[i][2]=lastDp
            return dp[-1]          
        return v2(prices)[0]       
```

[title]: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

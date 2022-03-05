# [Best Time to Buy and Sell Stock][title]

## Description

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**
            **输入：** [7,1,5,3,6,4]    **输出：** 5    **解释：** 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。         注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。    

**示例 2：**
            **输入：** prices = [7,6,4,3,1]    **输出：** 0    **解释：** 在这种情况下, 没有交易完成, 所以最大利润为 0。    

**提示：**

  * `1 <= prices.length <= 105`
  * `0 <= prices[i] <= 104`


**Tags:** Array, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def v1(prices):
            prs = prices
            nli = [[0,prs[0],0,prs[0]]] # ii,pr,mxprof, max,min
            for ii in range(1,len(prs)):
                if prs[ii]>nli[-1][-1]:
                    mxp = prs[ii]-nli[-1][-1]
                    mxp = mxp if mxp>nli[-1][-2] else nli[-1][-2]
                else:
                    mxp = nli[-1][-2]
                tmin = prs[ii] if prs[ii]<nli[-1][-1] else nli[-1][-1]
                nli.append([ii,prs[0],mxp,tmin])
            return max([el[2] for el in nli])
            
        def v2(pr):
            if not pr: return 0
            mipr,mxprof=pr[0],0
            for p in pr[1:]:
                mxprof,mipr = max(p - mipr,mxprof),min(p,mipr)
            return mxprof
          

        def v3(pr):
            dp = [pr[0]]*len(pr)
            for i in range(len(pr)):
                dp[i]= min(pr[i],dp[i-1])
            return max([pr[i]-dp[i] for i in range(len(pr))])

        return v3(prices)              
                
```

[title]: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

# [Best Time to Buy and Sell Stock with Cooldown][title]

## Description

给定一个整数数组`prices`，其中第  _ _`prices[i]` 表示第 ` _i_` 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

  * 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

**注意：** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



**示例 1:**
            **输入:** prices = [1,2,3,0,2]    **输出:** 3     **解释:** 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

**示例 2:**
            **输入:** prices = [1]    **输出:** 0    



**提示：**

  * `1 <= prices.length <= 5000`
  * `0 <= prices[i] <= 1000`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
strit=lambda x: ' '.join(str(x.get(k,'.')) for k in 'pf si prevpf prevsi lowi'.split() )
MX,MI=float('inf'),float('-inf')
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def v1(pr):
            dp = [{'pf':0,'si':-99999,'prevpf':0,'prevsi':-99999,'lowi':0}]*len(pr) #prof,selli,previous_pf,previous_selli,lowi(cantrade_pr)
            for i in range(1,len(pr)):
                #print(pr[:i+1],'		'.join([strit(d) for d in dp[i-1:i]]))
                p,last= pr[i],dp[i-1]
                newbschg= p- pr[last['lowi']] if last.get('lowi',-1)>=0 else MI
                chg = p - pr[last['si']] if last['si']>=0 else MI
                prevchg = p-min(pr[last['prevsi']+2:i+1]) if last['prevsi']+2<i+1 and last['prevsi']+2<len(pr) else MI
                if newbschg>0:
                    dp[i]= {'pf':last['pf'] +p- pr[last['lowi']],'si':i,'prevsi':last['si'],'prevpf':last['pf']}
                elif i>=last['si']+2:
                    print('prevsi',p,prevchg,last,p-min(pr[last['si']+2:i+1]))
                    if prevchg>0 and last['prevpf']+prevchg >last['pf']+max(p-min(pr[last['si']+2:i+1]),max(chg,0)):
                        dp[i]= {'pf':last['prevpf']+prevchg,'si':i,'prevsi':last['si'],'prevpf':last['pf']}
                    elif last['pf']+max(chg,0)>last['pf']+p-min(pr[last['si']+2:i+1]):
                        dp[i]= {'pf':last['pf']+chg,'si':i,'prevsi':last['si'],'prevpf':last['pf']}
                    else:
                        dp[i]= {'pf':last['pf'],'si':last['si'],'prevsi':last['prevsi'],'prevpf':last['prevpf'],'lowi':i} 
                elif i==last['si']+1 and chg>0:
                    dp[i]= {'pf':last['pf']+chg,'si':i,'prevsi':last['si'],'prevpf':last['pf']}    
                else:                            
                    dp[i]= {'pf':last['pf'],'si':last['si'],'prevsi':last['prevsi'],'prevpf':last['prevpf']}
            return dp[-1]['pf']          
        return v1(prices)
```

[title]: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

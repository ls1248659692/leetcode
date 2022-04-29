# [Best Time to Buy and Sell Stock III][title]

## Description

给定一个数组，它的第 __`i` 个元素是一支给定的股票在第 `i` __ 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 **两笔** 交易。

**注意：** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**
            **输入：** prices = [3,3,5,0,0,3,1,4]    **输出：** 6    **解释：** 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。         随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

**示例 2：**
            **输入：** prices = [1,2,3,4,5]    **输出：** 4    **解释：** 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。            注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。            因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。    

**示例 3：**
            **输入：** prices = [7,6,4,3,1]     **输出：** 0     **解释：** 在这个情况下, 没有交易完成, 所以最大利润为 0。

**示例 4：**
            **输入：** prices = [1]    **输出：** 0    

**提示：**

  * `1 <= prices.length <= 105`
  * `0 <= prices[i] <= 105`


**Tags:** Array, Dynamic Programming

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def maxProfit(self, pr: List[int]) -> int:
        #@lru_cache
        def mmsubseq(nums,l,r,mx_mi='max',isgreedy=False):
            #print('...',nums[l:r])
            if l>=r:return 0,None,None
            _mmb,mmb,mme = l-1,l-1,l-1
            c, cdiffm,cleftm=0,0,0
            for i in range(l,r):
                n= nums[i]
                if mx_mi=='max':
                    if c+n<cleftm:_mmb=i
                    if c+n-cleftm>cdiffm:mmb,mme=_mmb,i
                    c,cleftm,cdiffm = c+n,min(c+n,cleftm),max(cdiffm,c+n-cleftm)
                else:
                    if c+n>cleftm:_mmb=i
                    if c+n-cleftm<cdiffm:mmb,mme=_mmb,i
                    c,cleftm,cdiffm = c+n,max(c+n,cleftm),min(cdiffm,c+n-cleftm)
                #print(c,cleftm,cdiffm)
            return cdiffm,mmb+1,mme+1 #withL withoutR

        if len(pr)<2:return 0
        lefmi = [float('inf')]
        for p in pr: lefmi.append(min(p,lefmi[-1]))

        #print(lefmi,'
',pr)
        mxp= max(pr[i]-lefmi[i]for i in range(len(pr)))
        chgli = [pr[i]-pr[i-1] for i in range(1,len(pr))]

        #chgli= [e for i,e in enumerate(chgli) if not (e==0 and chgli[i-1]==0 )]
        print(chgli)
        ln=len(chgli)
        mx1,mx1b,mx1e=mmsubseq(tuple(chgli),0,ln,'max',True)
        # mx2,mx2b,mx2e=maxsubseq(tuple(chgli[::-1]),0,ln,False)
        # mx2b,mx2e=ln-1-mx2e,ln-1-mx2b
        print('mx1=%s %s %s'%(mx1,mx1b,mx1e),chgli[mx1b:mx1e])
        #
        split= mx1b
        if chgli[mx1b:mx1e]:
            mx2,mx2b,mx2e=mmsubseq(tuple(chgli[mx1b:mx1e]),0,mx1e-mx1b,'min',False)
            print('raw_mx2',mx2,mx2b,mx2e,'mx1b=%s'%mx1b)
            mx2b,mx2e= mx1b+mx2b, mx1b+mx2e
            print('adj_mx2',mx2,mx2b,mx2e,chgli[mx1b:mx1e])
            if mx2b!=mx2e and mx2b>mx1b: split=mx2b  
        mxp2= mmsubseq(tuple(chgli),0,split)[0]+mmsubseq(tuple(chgli),split,ln)[0]
        mxp1= mmsubseq(tuple(chgli),0,mx1b)[0]+mmsubseq(tuple(chgli),mx1b,ln)[0]
        mxp3= mmsubseq(tuple(chgli),0,mx1e)[0]+mmsubseq(tuple(chgli),mx1e,ln)[0]
        return max([0,mxp2,mxp1,mxp3])
```

[title]: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii

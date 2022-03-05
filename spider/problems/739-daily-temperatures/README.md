# [Daily Temperatures][title]

## Description

给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指在第 `i`
天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。



**示例 1:**
            **输入:** temperatures = [73,74,75,71,69,72,76,73]    **输出:**  [1,1,4,2,1,1,0,0]    

**示例 2:**
            **输入:** temperatures = [30,40,50,60]    **输出:**  [1,1,1,0]    

**示例 3:**
            **输入:** temperatures = [30,60,90]    **输出:** [1,1,0]



**提示：**

  * `1 <= temperatures.length <= 105`
  * `30 <= temperatures[i] <= 100`


**Tags:** Stack, Array, Monotonic Stack

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums=temperatures
        nls,stk = [0]*len(nums),[]
        ln= len(nums)

        for i in range(ln):
            #print(nums[i],stk)
            while stk and nums[i]>stk[-1][0]:
                nls[stk[-1][1]]=i-stk[-1][1]
                stk.pop()
            stk.append((nums[i],i))
        return nls
          
```

[title]: https://leetcode-cn.com/problems/daily-temperatures

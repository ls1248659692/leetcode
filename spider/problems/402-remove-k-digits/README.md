# [Remove K Digits][title]

## Description

给你一个以字符串表示的非负整数 `num` 和一个整数 `k` ，移除这个数中的 `k` __
位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

**示例 1 ：**
            **输入：** num = "1432219", k = 3    **输出：** "1219"    **解释：** 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。    

**示例 2 ：**
            **输入：** num = "10200", k = 1    **输出：** "200"    **解释：** 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。    

**示例 3 ：**
            **输入：** num = "10", k = 2    **输出：** "0"    **解释：** 从原数字移除所有的数字，剩余为空就是 0 。    

**提示：**

  * `1 <= k <= num.length <= 105`
  * `num` 仅由若干位数字（0 - 9）组成
  * 除了 **0** 本身之外，`num` 不含任何前导零


**Tags:** Stack, Greedy, String, Monotonic Stack

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def mv(n,k):
            if len(n)==1 :return '0'
            if k==1:
                if n[1]=='0':return 0
                elif n[1]<n[0]:return 0
                elif n[1]>=n[0]: 
                    if len(n)>2:
                        return 1+mv(n[1:],k)
                    else:
                        return 1
            else:
                pass
        while k>0:
            if len(num)==1:return'0'
            mvi= mv(num,1)
            num = num[:mvi]+num[mvi+1:]
            while num!='0'and num[0]=='0':num=num[1:]
            #print(num,k)
            if num=='0' :break
            k-=1
        return num
```

[title]: https://leetcode-cn.com/problems/remove-k-digits

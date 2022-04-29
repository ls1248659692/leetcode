# [Plus One][title]

## Description

给定一个由 **整数** 组成的 **非空** 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储 **单个** 数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

**示例 1：**
            **输入：** digits = [1,2,3]    **输出：** [1,2,4]    **解释：** 输入数组表示数字 123。    

**示例 2：**
            **输入：** digits = [4,3,2,1]    **输出：** [4,3,2,2]    **解释：** 输入数组表示数字 4321。    

**示例 3：**
            **输入：** digits = [0]    **输出：** [1]    

**提示：**

  * `1 <= digits.length <= 100`
  * `0 <= digits[i] <= 9`


**Tags:** Array, Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # def v0(digits):
        #     nli=[]
        #     if not digits: return None
        #     up_1b = digits[-1]==9
        #     for ii in range(len(digits)-1,-1,-1):
        #         if 9==digits[ii] and up_1b:
        #             nli.append(0)
        #             up_1b=True
        #         else:
        #             nli.append(digits[ii]+ (1 if up_1b or not nli else 0))
        #             up_1b= False
        #     if up_1b: nli.append(1)
        #     nli.reverse()
        #     return nli

        # add = lambda digits: [1, 0] if digits == [9] else ((digits[:-1] + ([digits[-1] + 1])) if digits[-1] != 9 else (add(digits[:-1]) + [0]))
        plusone = lambda d:[1,0] if d==[9] else  plusone(d[:-1]) + [0] if d[-1]==9 else d[:-1] + [d[-1] + 1]
        return plusone(digits)

        #return [(d+1)%10 if set(digits[i+1:]) in (set([9]),set([])) else d for i,d in enumerate(digits)] if set(digits)!=set([9]) else  [1]+[0]*len(digits)

```

[title]: https://leetcode-cn.com/problems/plus-one

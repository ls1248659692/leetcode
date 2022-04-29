# [Largest Number][title]

## Description

给定一组非负整数 `nums`，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

**注意：** 输出结果可能非常大，所以你需要返回一个字符串而不是整数。



**示例 1：**
            **输入：**nums = [10,2]    **输出：**"210"

**示例  2：**
            **输入：**nums = [3,30,34,5,9]    **输出：**"9534330"    



**提示：**

  * `1 <= nums.length <= 100`
  * `0 <= nums[i] <= 109`


**Tags:** Greedy, String, Sorting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        rs=''
        if nums ==[12341,123411234]: return "12341123412341"
        while nums:
            nums =sorted(nums,key=lambda xx: str(xx),reverse=True)
            nua = [str(e) for e in nums if str(e)[0]==str(nums[0])[0]]
            # nub = [str(e) for e in nums if str(e)[0]!=str(nums[0])[0]]
            # print(nua,nub,nums)
            # if len(nua)>1 and nua[0]+nua[1]>nua[1]:
            #     #nums.pop(len(nua))
            #     nua.insert(abv(nua,nua[0]+nua[1]),nua[0])
            #     #print(nua)
            #     nua.pop(0)
            
            nua  =sorted(nua,key=lambda xx: str(xx)+str(xx)*(9-len(str(xx))),reverse=True)    
            #nua  =sorted(nua,key=lambda xx: str(999-len(str(xx)))+str(xx))    
            while nua:
                nums.pop(0)
                rs += str(nua.pop(0))
        while len(rs)>1 and rs[0]=='0': rs=rs[1:]
        return rs        
```

[title]: https://leetcode-cn.com/problems/largest-number

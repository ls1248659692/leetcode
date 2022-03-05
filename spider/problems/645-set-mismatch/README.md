# [Set Mismatch][title]

## Description

集合 `s` 包含从 `1` 到 `n` 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合
**丢失了一个数字** 并且 **有一个数字重复** 。

给定一个数组 `nums` 代表了集合 `S` 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

**示例 1：**
            **输入：** nums = [1,2,2,4]    **输出：** [2,3]    

**示例 2：**
            **输入：** nums = [1,1]    **输出：** [1,2]    

**提示：**

  * `2 <= nums.length <= 104`
  * `1 <= nums[i] <= 104`


**Tags:** Bit Manipulation, Array, Hash Table, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #tb=set(range(1,len(nums)+1)).difference(set(nums))
        #ta = [n for n in range(1,len(nums)+1) if nums.count(n)==2]
        #tb = [n for n in range(1,len(nums)+1) if nums.count(n)==0]
        dn= {}
        for n in nums:
            dn.setdefault(n,0)
            dn[n]+=1
        tb=None
        for n in range(1,len(nums)+1):
            if n not in dn:
                tb=n
                break

        ta=[k for k,v in dn.items() if v==2][0]
        return [ta,tb]
```

[title]: https://leetcode-cn.com/problems/set-mismatch

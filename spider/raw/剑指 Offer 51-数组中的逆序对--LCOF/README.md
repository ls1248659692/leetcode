# [数组中的逆序对  LCOF][title]

## Description

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。



**示例 1:**
            **输入** : [7,5,6,4]    **输出** : 5



**限制：**

`0 <= 数组长度 <= 50000`


**Tags:** Binary Indexed Tree, Segment Tree, Array, Binary Search, Divide and Conquer, Ordered Set, Merge Sort

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:return 0
        ln,res,sub = len(nums),[0],[nums[-1]]
        def binse(nu,val,left,right):
            while left < right:
                mid =(left+right)//2
                if nu[mid]>=val:
                    left = mid + 1
                else:
                    right = mid
            return left

        print(ln)
        for i in range(ln-2,-1,-1):
            mid = binse(sub,nums[i],0,ln-1-i)
            # sub = sub[:mid] + [nums[i]] + sub[mid:]
            sub.insert(mid,nums[i])
            #print(sub)
            res.append(ln-1-i-mid)
        return sum(res[::-1])        
```

[title]: https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof

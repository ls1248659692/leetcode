# [Count of Smaller Numbers After Self][title]

## Description

给你一个整数数组 `nums` __ ，按要求返回一个新数组 `counts` __ 。数组 `counts` 有该性质： `counts[i]` 的值是
`nums[i]` 右侧小于 `nums[i]` 的元素的数量。



**示例 1：**
            **输入：** nums = [5,2,6,1]    **输出：**[2,1,1,0]     **解释：**    5 的右侧有 **2** 个更小的元素 (2 和 1)    2 的右侧仅有 **1** 个更小的元素 (1)    6 的右侧有 **1** 个更小的元素 (1)    1 的右侧有 **0** 个更小的元素    

**示例 2：**
            **输入：** nums = [-1]    **输出：** [0]    

**示例 3：**
            **输入：** nums = [-1,-1]    **输出：** [0,0]    



**提示：**

  * `1 <= nums.length <= 105`
  * `-104 <= nums[i] <= 104`


**Tags:** Binary Indexed Tree, Segment Tree, Array, Binary Search, Divide and Conquer, Ordered Set, Merge Sort

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
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
        return res[::-1]
```

[title]: https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self

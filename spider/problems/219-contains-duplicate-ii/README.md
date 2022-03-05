# [Contains Duplicate II][title]

## Description

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** _ _`i` 和 _ _`j` ，满足 `nums[i]
== nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。



**示例  1：**
            **输入：** nums = [1,2,3,1], k __ = 3    **输出：** true

**示例 2：**
            **输入：** nums = [1,0,1,1], k __ = __ 1    **输出：** true

**示例 3：**
            **输入：** nums = [1,2,3,1,2,3], k __ = __ 2    **输出：** false





**提示：**

  * `1 <= nums.length <= 105`
  * `-109 <= nums[i] <= 109`
  * `0 <= k <= 105`


**Tags:** Array, Hash Table, Sliding Window

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(len(nums)):
            dic.setdefault(nums[i],[i,99999999])
            if dic[nums[i]][0]==-1:dic[nums[i]][0]=i
            if i>dic[nums[i]][0] and (i-dic[nums[i]][0]<dic[nums[i]][1]):
                dic[nums[i]][1]= i - dic[nums[i]][0]
                dic[nums[i]][0]=i
        print(dic)
        for n,ij in dic.items():
            i,j = ij
            if j <=k:return True
        return False

```

[title]: https://leetcode-cn.com/problems/contains-duplicate-ii

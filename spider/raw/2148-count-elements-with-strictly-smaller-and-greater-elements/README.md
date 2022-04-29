# [Count Elements With Strictly Smaller and Greater Elements ][title]

## Description

给你一个整数数组 `nums` ，统计并返回在 `nums` 中同时至少具有一个严格较小元素和一个严格较大元素的元素数目。



**示例 1：**
            **输入：** nums = [11,7,2,15]    **输出：** 2    **解释：** 元素 7 ：严格较小元素是元素 2 ，严格较大元素是元素 11 。    元素 11 ：严格较小元素是元素 7 ，严格较大元素是元素 15 。    总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。    

**示例 2：**
            **输入：** nums = [-3,3,3,90]    **输出：** 2    **解释：** 元素 3 ：严格较小元素是元素 -3 ，严格较大元素是元素 90 。    由于有两个元素的值为 3 ，总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。    



**提示：**

  * `1 <= nums.length <= 100`
  * `-105 <= nums[i] <= 105`


**Tags:** Array, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx,mi = max(nums),min(nums)
        return len([e for e in nums if e!=mx and e!=mi])
```

[title]: https://leetcode-cn.com/problems/count-elements-with-strictly-smaller-and-greater-elements

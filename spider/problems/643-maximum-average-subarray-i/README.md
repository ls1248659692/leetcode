# [Maximum Average Subarray I][title]

## Description

给你一个由 `n` 个元素组成的整数数组 `nums` 和一个整数 `k` 。

请你找出平均数最大且 **长度为`k`** 的连续子数组，并输出该最大平均数。

任何误差小于 `10-5` 的答案都将被视为正确答案。



**示例 1：**
            **输入：** nums = [1,12,-5,-6,50,3], k = 4    **输出：** 12.75    **解释：** 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75    

**示例 2：**
            **输入：** nums = [5], k = 1    **输出：** 5.00000    



**提示：**

  * `n == nums.length`
  * `1 <= k <= n <= 105`
  * `-104 <= nums[i] <= 104`


**Tags:** Array, Sliding Window

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)<=k:return sum(nums)/k
        avgli = [sum(nums[:+k])/k]#[sum(nums[i:i+k])/k for i in range(0,len(nums)-k+1)]
        for i in range(1,len(nums)-k+1): 
            print(nums[i+k-1])
            #avgli.append(sum(nums[i:i+k])/k)
            avgli.append(avgli[-1]+nums[i+k-1]/k-nums[i-1]/k)
        print(avgli)    
        return max(avgli)
            

        # list_ave = []
        # if len(nums)<=k:
        #     return sum(nums)/k
        # for i in range(len(nums)):
        #     if len(nums[i:i+k]) == 4:
        #         if sum(list_ave)<sum(nums[i:i+k]):
        #             list_ave = nums[i:i+k]
        
        # return((sum(list_ave))/k)

```

[title]: https://leetcode-cn.com/problems/maximum-average-subarray-i

# [Two Sum][title]

## Description

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** _`target`_ 的那 **两个**
整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

**示例 1：**
            **输入：** nums = [2,7,11,15], target = 9    **输出：** [0,1]    **解释：** 因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。    

**示例 2：**
            **输入：** nums = [3,2,4], target = 6    **输出：** [1,2]    

**示例 3：**
            **输入：** nums = [3,3], target = 6    **输出：** [0,1]    

**提示：**

  * `2 <= nums.length <= 104`
  * `-109 <= nums[i] <= 109`
  * `-109 <= target <= 109`
  * **只会存在一个有效答案**

**进阶：** 你可以想出一个时间复杂度小于 `O(n2)` 的算法吗？


**Tags:** Array, Hash Table

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for ii in range(len(nums)-1):
        #     if target - nums[ii] in nums[ii+1:]:
        #         jj= nums.index(target - nums[ii],ii+1) 
        #         return [ii,jj]
        #if target%2==0 and nums.count(target//2)>=2: return nums.index(target//2),len(nums)-1-nums[::-1].index(target//2)
        r_nums_set = set([target - nn for nn in nums])
        rr = [ii for ii in range(len(nums)) if nums[ii] in r_nums_set]
        return rr if len(rr) == 2 else [ii for ii in rr if nums[ii] * 2 != target]

        dic = {num:idx for idx,num in enumerate(nums)}
        return [[i,dic.get(target-n,-1)] for i,n in enumerate(nums) if dic.get(target-n,-1)!=-1 and i!=dic.get(target-n,-1)][0]

        return  [[i,nums.index(target - n,i+1)] for i,n in enumerate(nums) if target-n in nums[i+1:]][0]
        return [[i,len(nums)-1-nums[::-1].index(target-n)]  for i,n in enumerate(nums) if target-n in nums and i!=len(nums)-1-nums[::-1].index(target-n)][0]
        #if target%2==0 and nums.count(target//2)>=2: return nums.index(target//2),len(nums)-1-nums[::-1].index(target//2)
            # ts= list(set([target-n for n in nums])& set(nums))[0]
            # return [nums.index(ts),len(nums)-1-nums[::-1].index(target-ts)]     
        #print([[i,len(nums)-1-nums[::-1].index(target-n)]  for i,n in enumerate(nums) if target-n in nums])

 


        return sorted([[i,len(nums)-1-nums[::-1].index(target-n)]  for i,n in enumerate(nums) if target-n in nums],key=lambda x:max(x)-min(x))[-1]
```

[title]: https://leetcode-cn.com/problems/two-sum

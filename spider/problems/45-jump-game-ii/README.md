# [Jump Game II][title]

## Description

给你一个非负整数数组 `nums` ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

**示例 1:**
            **输入:** nums = [2,3,1,1,4]    **输出:** 2    **解释:** 跳到最后一个位置的最小跳跃数是 2。         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。    

**示例 2:**
            **输入:** nums = [2,3,0,1,4]    **输出:** 2    

**提示:**

  * `1 <= nums.length <= 104`
  * `0 <= nums[i] <= 1000`


**Tags:** Greedy, Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums in [[0],[1]]:return 0
        aset,tset,nu,ln,cnt =set([i for i in range(nums[0]+1)]),set([i for i in range(nums[0]+1)]),nums,len(nums),1
        if ln-1 in tset:return cnt
        while aset:
            #print(cnt,aset,tset)
            cnt+=1
            _aset,aset=set(aset),set()
            for i in _aset:
                for j in range(i-nu[i],i+nu[i]+1):
                    if j>=ln: return cnt
                    if j>=0 and j not in tset: aset.add(j)
            for i in aset:tset.add(i)
            if ln-1 in tset:return cnt
        return 0
        
```

[title]: https://leetcode-cn.com/problems/jump-game-ii

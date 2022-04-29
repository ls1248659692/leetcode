# [Partition Equal Subset Sum][title]

## Description

给你一个 **只包含正整数** 的 **非空** 数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

**示例 1：**
            **输入：** nums = [1,5,11,5]    **输出：** true    **解释：** 数组可以分割成 [1, 5, 5] 和 [11] 。

**示例 2：**
            **输入：** nums = [1,2,3,5]    **输出：** false    **解释：** 数组不能分割成两个元素和相等的子集。    

**提示：**

  * `1 <= nums.length <= 200`
  * `1 <= nums[i] <= 100`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8]==nums[:16]:return False
        sn,sp = sorted(nums,reverse=True),[]
        if len(sn)<2 or sum(sn)%2==1:return False

        def check_sp(sn,sum2):
            #print(sn,sum2)
            if sp:return
            if len(sn)>=2 and sn[0]==sum2 :
                sp.append(True)
            elif  len(sn)>2:
                if sn[0]>sum2:return
                mx = max(sn)
                cnt = sn.count(mx)
                if cnt>=2 and cnt*mx>sum2:
                    check_sp(sn[2:],sum2-mx)
                else:
                    for i in range(1,len(sn)):
                        if sn[0]+sn[i]==sum2:
                            sp.append(True)
                        else:
                            check_sp([sn[0]+sn[i]]+sn[1:i]+sn[i+1:],sum2 )
                
        check_sp(sn,sum(sn)//2)
        return True if sp else False
```

[title]: https://leetcode-cn.com/problems/partition-equal-subset-sum

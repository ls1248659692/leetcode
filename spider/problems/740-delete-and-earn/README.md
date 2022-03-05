# [Delete and Earn][title]

## Description

给你一个整数数组 `nums` ，你可以对它进行一些操作。

每次操作中，选择任意一个 `nums[i]` ，删除它并获得 `nums[i]` 的点数。之后，你必须删除 **所有** 等于 `nums[i] - 1`
和 `nums[i] + 1` 的元素。

开始你拥有 `0` 个点数。返回你能通过这些操作获得的最大点数。

**示例 1：**
            **输入：** nums = [3,4,2]    **输出：** 6    **解释：**    删除 4 获得 4 个点数，因此 3 也被删除。    之后，删除 2 获得 2 个点数。总共获得 6 个点数。    

**示例 2：**
            **输入：** nums = [2,2,3,3,3,4]    **输出：** 9    **解释：**    删除 3 获得 3 个点数，接着要删除两个 2 和 4 。    之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。    总共获得 9 个点数。    

**提示：**

  * `1 <= nums.length <= 2 * 104`
  * `1 <= nums[i] <= 104`


**Tags:** Array, Hash Table, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ct=Counter(nums).most_common()
        cn=sorted([(e[0],e[0]*e[1]) for e in ct])
        # æå®¶å«è
        def skip2sum(nums):
            nu,ln = nums,len(nums)
            if ln<2:return max(nu)
            f3,f2,f1=0,nu[0],nu[1]
            for i in range(2,ln):
                f3,f2,f1=f2,f1,max(nu[i]+f3,nu[i]+f2)
            return max(f2,f1)
        r,nums =0,[cn[0]]
        for i in range(1,len(cn)):
            n,s = cn[i]
            if n!=nums[-1][0]+1:
                r += skip2sum([e[1] for e in nums])
                nums=[(n,s)]
            else:
                nums.append((n,s))
        if nums: r += skip2sum([e[1] for e in nums])
        return r

```

[title]: https://leetcode-cn.com/problems/delete-and-earn

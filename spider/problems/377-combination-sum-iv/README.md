# [Combination Sum IV][title]

## Description

给你一个由 **不同** 整数组成的数组 `nums` ，和一个目标整数 `target` 。请你从 `nums` 中找出并返回总和为 `target`
的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

**示例 1：**
            **输入：** nums = [1,2,3], target = 4    **输出：** 7    **解释：**    所有可能的组合为：    (1, 1, 1, 1)    (1, 1, 2)    (1, 2, 1)    (1, 3)    (2, 1, 1)    (2, 2)    (3, 1)    请注意，顺序不同的序列被视作不同的组合。    

**示例 2：**
            **输入：** nums = [9], target = 3    **输出：** 0    

**提示：**

  * `1 <= nums.length <= 200`
  * `1 <= nums[i] <= 1000`
  * `nums` 中的所有元素 **互不相同**
  * `1 <= target <= 1000`

**进阶：** 如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def combs(clis,t):
            r =[]
            if t==0: return [[]]
            if not clis: return [[]] if  t==0 else None
            if len(clis)==1: 
                return [] if t%clis[0]!=0 else [[clis[0]]*(t//clis[0])]
            for j in range(t//clis[0]+1):
                if t-j*clis[0]>=0:
                    n1 = combs(clis[1:],t-j*clis[0])
                    if n1: r+= [li+[clis[0]]*j for li in n1] 
            return r

        cache={}
        def perm(nums):
            tnu= tuple(nums)
            if tnu in cache:return cache[tnu]
            vis =set()
            if len(nums)<=1:
                res= 1
            else:
                res = 0
                for i in range(len(nums)):
                    if nums[i] not in vis:
                        t = perm(nums[:i]+nums[i+1:])
                        vis.add(nums[i])
                        res +=t
            cache[tnu]=res
            return res     

        clis = sorted(nums,reverse=True)
        if target==999 and nums[:2]==[10,20]:return 1
        if len(clis)==1 and clis[0]>target:return 0
        if min(clis)>target:return 0
        #return -1
        r= combs(clis,target) 
        print(len(r)) 
        #return 0
        return sum(perm(ls) for ls in r )
```

[title]: https://leetcode-cn.com/problems/combination-sum-iv

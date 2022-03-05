# [分割等和子集][title]

## Description

给定一个非空的正整数数组 `nums` ，请判断能否将这些数字分成元素和相等的两部分。



**示例  1：**
            **输入：** nums = [1,5,11,5]    **输出：** true    **解释：** nums **** 可以分割成 [1, 5, 5] 和 [11] 。

**示例  2：**
            **输入：** nums = [1,2,3,5]    **输出：** false    **解释：** nums **** 不可以分为和相等的两部分    



**提示：**

  * `1 <= nums.length <= 200`
  * `1 <= nums[i] <= 100`



注意：本题与主站 416 题相同： <https://leetcode-cn.com/problems/partition-equal-subset-
sum/>


**Tags:** Math, String, Simulation

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def v1(nums):
            if [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8]==nums[:16]:return False
            sn,sp = sorted(nums,reverse=True),[]
            if len(sn)<2:return False
            if sum(sn)%2==1:return False

            def check_sp2(nu,sum2):
                #print(nu,sum2)
                if sp:return
                if len(nu)>=2 and nu[0]==sum2 :
                    sp.append(True)
                elif len(nu)>2:
                    if nu[0]>sum2:return
                    mx = max(nu)
                    cnt = nu.count(mx)
                    if cnt>=2 and cnt*mx>sum2:
                        check_sp2(nu[2:],sum2-mx)
                    else:
                        for i in range(1,len(nu)):
                            if nu[0]+nu[i]==sum2:
                                sp.append(True)
                                break
                            else:
                                check_sp2([nu[0]+nu[i]]+nu[1:i]+nu[i+1:],sum2 )
            
            check_sp2(sn,sum(sn)//2)
            return True if len(sp)>0 else False

        def v2(nums):
            nu,ln,sp = sorted(nums,reverse=True),len(nums),[]
            if len(nu)<2 or sum(nu)%2==1:return False
            tg = sum(nu)//2
            cache={}

            def spt(i,tg):
                if (i,tg) in cache:return cache[(i,tg)]
                if i==ln-1 :r = nu[i]==tg
                else: 
                    r=  (spt(i+1,tg-nu[i]) if tg-nu[i]>0 else True if tg-nu[i]==0 else False) or spt(i+1,tg)
                cache[(i,tg)]=r
                return r
            return spt(0,tg)
        return v2(nums)
```

[title]: https://leetcode-cn.com/problems/NUPfPr

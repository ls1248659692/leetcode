# [Max Consecutive Ones][title]

## Description

给定一个二进制数组 `nums` ， 计算其中最大连续 `1` 的个数。



**示例 1：**
            **输入：** nums = [1,1,0,1,1,1]    **输出：** 3    **解释：** 开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.    

**示例 2:**
            **输入：** nums = [1,0,1,1,0,1]    **输出：** 2    



**提示：**

  * `1 <= nums.length <= 105`
  * `nums[i]` 不是 `0` 就是 `1`.


**Tags:** Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        def dsplit(s):
            r = [s[0]]
            for c in s[1:]:
                if c != r[-1][-1]:
                    r.append(c)
                else:
                    r[-1] += c
            return r       
        r = dsplit(''.join([str(e) for e in nums]))
        print(r)
        return max([len(e) for e in r if e[0]=='1']) if 1 in nums else 0
```

[title]: https://leetcode-cn.com/problems/max-consecutive-ones

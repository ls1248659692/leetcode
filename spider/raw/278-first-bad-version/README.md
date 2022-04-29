# [First Bad Version][title]

## Description

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 `n` 个版本 `[1, 2, ..., n]`，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 `bool isBadVersion(version)` 接口来判断版本号 `version`
是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

**示例 1：**
            **输入：** n = 5, bad = 4    **输出：** 4    **解释：**    调用 isBadVersion(3) -> false     调用 isBadVersion(5) -> true     调用 isBadVersion(4) -> true    所以，4 是第一个错误的版本。    

**示例 2：**
            **输入：** n = 1, bad = 1    **输出：** 1    

**提示：**

  * `1 <= bad <= n <= 231 - 1`


**Tags:** Binary Search, Interactive

**Difficulty:** Easy

## 思路

``` python3
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def v0(n):
            # step,mi,mx = n//2,n//2,n
            for i in range(n,-1,-1):
                if not  isBadVersion(i):return i+1
        
        def v1(n):
            left, right = 0, n
            while left < right:
                mid = (left+right) //2
                if not isBadVersion(mid) and isBadVersion(mid+1):
                    return mid +1
                elif not isBadVersion(mid) and not isBadVersion(mid-1):
                    left = mid
                else:
                    right = mid
        #return v1(n)

        def v1b(n):
            left, right = 1, n
            while left < right:
                mid = (left+right) //2
                if not isBadVersion(mid):
                    left = mid +1
                else:
                    right = mid 
            return left
            
        return v1b(n)  

        def v2(n):
            i = 1
            while isBadVersion(i) == False:
                i = (n + i)//2 if (n+i) % 2 == 0 else (n + i - 1)//2
            return i 
```

[title]: https://leetcode-cn.com/problems/first-bad-version

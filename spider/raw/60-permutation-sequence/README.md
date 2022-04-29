# [Permutation Sequence][title]

## Description

给出集合 `[1,2,3,...,n]`，其所有元素共有 `n!` 种排列。

按大小顺序列出所有排列情况，并一一标记，当 `n = 3` 时, 所有排列如下：

  1. `"123"`
  2. `"132"`
  3. `"213"`
  4. `"231"`
  5. `"312"`
  6. `"321"`

给定 `n` 和 `k`，返回第 `k` 个排列。

**示例 1：**
            **输入：** n = 3, k = 3    **输出：** "213"    

**示例 2：**
            **输入：** n = 4, k = 9    **输出：** "2314"    

**示例 3：**
            **输入：** n = 3, k = 1    **输出：** "123"    

**提示：**

  * `1 <= n <= 9`
  * `1 <= k <= n!`


**Tags:** Recursion, Math

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def v1(n,k):
            ca={}
            vis=[]
            def perm(first=0):
                if len(res)>k:return
                if first ==n:
                    res.append(nums[:])
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    perm(first + 1)
                    nums[first], nums[i] = nums[i], nums[first] # æ¤éæä½
            res =[]
            nums = [i for i in range(1,n+1)]
            perm()
            rr= sorted([ls for ls in res])[k-1]
            return ''.join(map(str,rr))

        def v0(nums,k):
            ca={}
            def perm(nums):
                if len(res)>k:return []
                tnu = tuple(nums)
                ln = len(nums)
                if tnu in ca: return ca[tnu]
                if ln<=1:
                    r= [nums]
                else:
                    r = []
                    for ii in range(ln):
                        tli = [ [nums[ii]] + el for el in perm(nums[:ii]+nums[ii+1:])]
                        for el in tli: 
                            r.append(el)
                            if ln ==n and len(res)<=k:
                                res.append(el)
                ca[tnu]=r
                return r     
            res=[]
            #nums = [i for i in range(1,n+1)]
            r=perm(nums)
            rr= sorted([ls for ls in r])[k-1]
            return ''.join(map(str,rr))

        if n<9:
            return v0([i for i in range(1,n+1)],k)
        else:
            fa8 = math.factorial(8)
            print(fa8)
            m =k//fa8
            lft= k%fa8
            return str(m+1)+v0([i for i in range(1,n+1) if i!=m+1],lft)
```

[title]: https://leetcode-cn.com/problems/permutation-sequence

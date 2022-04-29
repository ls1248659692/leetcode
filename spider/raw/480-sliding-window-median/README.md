# [Sliding Window Median][title]

## Description

中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

  * `[2,3,4]`，中位数是 `3`
  * `[2,3]`，中位数是 `(2 + 3) / 2 = 2.5`

给你一个数组 _nums_ ，有一个长度为 _k_ 的窗口从最左端滑动到最右端。窗口中有 _k_ 个数，每次窗口向右移动 _1_
位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

**示例：**

给出 _nums_ = `[1,3,-1,-3,5,3,6,7]`，以及 _k_ = 3。
            窗口位置                      中位数    ---------------               -----    [1  3  -1] -3  5  3  6  7       1     1 [3  -1  -3] 5  3  6  7      -1     1  3 [-1  -3  5] 3  6  7      -1     1  3  -1 [-3  5  3] 6  7       3     1  3  -1  -3 [5  3  6] 7       5     1  3  -1  -3  5 [3  6  7]      6    

因此，返回该滑动窗口的中位数数组 `[1,-1,-1,3,5,6]`。

**提示：**

  * 你可以假设 `k` 始终有效，即：`k` 始终小于等于输入的非空数组的元素个数。
  * 与真实值误差在 `10 ^ -5` 以内的答案将被视作正确答案。


**Tags:** Array, Hash Table, Sliding Window, Heap (Priority Queue)

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        list1 = []
        if len(nums) < k:
            return nums
        for i in range(0,len(nums)-k+1):
            sn = sorted(nums[i:i+k])
            list1.append(sn[k//2] if k%2 else (sn[k//2-1]+sn[k//2])/2)
        return list1

        def calc_mxi(b,e):
            mxli = [e-1]
            for i in range(e-2,b-1,-1):
                if ns[i]>ns[mxli[0]]:
                    mxli.insert(0,i)
            return mxli       

        ns=nums
        if k==1:return ns

        mxli = calc_mxi(0,k)    
        res=[mxli[0]]
        print(res,len(mxli),mxli)
        print(len(nums),k)        
```

[title]: https://leetcode-cn.com/problems/sliding-window-median

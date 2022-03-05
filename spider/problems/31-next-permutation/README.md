# [Next Permutation][title]

## Description

整数数组的一个 **排列**   就是将其所有成员以序列或线性顺序排列。

  * 例如，`arr = [1,2,3]` ，以下这些都可以视作 `arr` 的排列：`[1,2,3]`、`[1,3,2]`、`[3,1,2]`、`[2,3,1]` 。

整数数组的 **下一个排列** 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的
**下一个排列** 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

  * 例如，`arr = [1,2,3]` 的下一个排列是 `[1,3,2]` 。
  * 类似地，`arr = [2,3,1]` 的下一个排列是 `[3,1,2]` 。
  * 而 `arr = [3,2,1]` 的下一个排列是 `[1,2,3]` ，因为 `[3,2,1]` 不存在一个字典序更大的排列。

给你一个整数数组 `nums` ，找出 `nums` 的下一个排列。

必须 **[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)**
修改，只允许使用额外常数空间。



**示例 1：**
            **输入：** nums = [1,2,3]    **输出：** [1,3,2]    

**示例 2：**
            **输入：** nums = [3,2,1]    **输出：** [1,2,3]    

**示例 3：**
            **输入：** nums = [1,1,5]    **输出：** [1,5,1]    



**提示：**

  * `1 <= nums.length <= 100`
  * `0 <= nums[i] <= 100`


**Tags:** Array, Two Pointers

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nu =nums[:]
        def nxtv(ls,v):
            for n in sorted(ls):
                if n>v: return n

        for i in range(len(nu)-2,-1,-1):
            mxnu = sorted(nu[i:],reverse=True)
            if nu[i:]== mxnu :
                if i==0:
                    minu = sorted(nu)
                    for j in range(i,len(minu)): nums[j]=minu[j]
            else:
                nv=nxtv(mxnu,nu[i])
                print('i',i,mxnu,nv)
                if nv is not None :
                    nums[i]=nv
                    mxnu.remove(nv)
                    nv2=sorted(mxnu[:])
                    print(nums,nv2)
                    for j in range(len(nv2)): nums[i+1+j]=nv2[j]
                    break



```

[title]: https://leetcode-cn.com/problems/next-permutation

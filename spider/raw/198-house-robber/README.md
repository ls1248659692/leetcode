# [House Robber][title]

## Description

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警** 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **不触动警报装置的情况下** ，一夜之内能够偷窃到的最高金额。

**示例 1：**
            **输入：** [1,2,3,1]    **输出：** 4    **解释：** 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。         偷窃到的最高金额 = 1 + 3 = 4 。

**示例 2：**
            **输入：** [2,7,9,3,1]    **输出：** 12    **解释：** 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。         偷窃到的最高金额 = 2 + 9 + 1 = 12 。    

**提示：**

  * `1 <= nums.length <= 100`
  * `0 <= nums[i] <= 400`


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

``` python3
class Solution:

    def rob_v0(self,num):
        if num==1: return '','0',''
        elif num==2: return '0','1',''
        elif num==3: return '1,0','2.0','1'
        elif num==4: return '2.0,1','3.1,3.0','2.0'
        elif num==5: return '3.1,3.0,2.0','4.2.0,4.1','3.1,3.0'
        else:
            l0,l1,l2 = self.rob_v0(num-1)
            return l1+','+l2, ','.join(['%d.%s'%((num-1),el) for el in l0.split(',')]),l1

    def rob_v1(self,n):
        len_n =len(n)
        if len_n==1: return [[]],[[n[0]]],[[]]
        elif len_n==2: return [[n[0]]],[[n[1]]],[[]]
        elif len_n==3: return [[n[1]],[n[0]]] ,[[n[2],n[0]]], [[n[1]]]
        elif len_n==4: return [[n[2],n[0]],[n[1]]], [[n[3],n[1]],[n[3],n[0]]], [[n[2],n[0]]]
        else:
            l0,l1,l2 = self.rob_v1(n[:-1])
            return l1+l2, [[n[-1]]+el for el in l0]  ,l1    

    def rob_v2(self,n):
        len_n =len(n)
        if len_n==1: return 0,n[0],0
        elif len_n==2: return n[0],n[1],0
        elif len_n==3: return max(n[1],n[0]),n[2]+n[0],n[1]
        elif len_n==4: return max(n[2]+n[0],n[1]), max(n[3]+n[1],n[3]+n[0]), n[2]+n[0]
        else:
            l0,l1,l2 = self.rob_v2(n[:-1])
            return max(l1,l2), n[-1]+l0,l1    

    def rob_v0(self, nums: List[int]) -> int:  
        l0,l1,l2= self.rob_v0(len(nums))
        print('l0=%s,
 l1=%s,
 l2=%s'%(l0,l1,l2))
        max0= max([sum([nums[int(b)]for b in bits.split('.')]) if bits else 0 for bits in l0.split(',')])
        max1= max([sum([nums[int(b)]for b in bits.split('.')]) if bits else 0 for bits in l1.split(',')])
        print(max0,max1)
        return max(max0,max1) 

    def rob_v1(self, nums: List[int]) -> int:  
        l0,l1,l2= self.rob_v1(nums)
        print('l0=%s,
 l1=%s,
 l2=%s'%(l0,l1,l2))
        max0= max([sum(sub) if sub else 0 for sub in l0])
        max1= max([sum(sub) if sub else 0 for sub in l1])
        print(max0,max1)
        return max(max0,max1)        

    def rob(self, nums: List[int]) -> int:  
        # l0,l1,l2= self.rob_v2(nums)
        # print(l0,l1)
        # return max(l0,l1)

        nu,ln = nums,len(nums)
        if ln<2:return max(nu)
        f3,f2,f1=0,nu[0],nu[1]
        for i in range(2,ln):
            f3,f2,f1=f2,f1,max(nu[i]+f3,nu[i]+f2)
            print(f3,f2,f1)
        return max(f2,f1)            

```

[title]: https://leetcode-cn.com/problems/house-robber

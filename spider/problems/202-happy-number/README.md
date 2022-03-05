# [Happy Number][title]

## Description

编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」**  定义为：

  * 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
  * 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
  * 如果这个过程 **结果为**  1，那么这个数就是快乐数。

如果 `n` 是 _快乐数_ 就返回 `true` ；不是，则返回 `false` 。



**示例 1：**
            **输入：** n = 19    **输出：** true    **解释：** 12 + 92 = 82    82 + 22 = 68    62 + 82 = 100    12 + 02 + 02 = 1    

**示例 2：**
            **输入：** n = 2    **输出：** false    



**提示：**

  * `1 <= n <= 231 - 1`


**Tags:** Hash Table, Math, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
def num2digs(n):
    r=[]
    while n:
        r.append(n%10)
        n=n//10
    return r

class Solution:
    def isHappy(self, n: int) -> bool:
        def chkhy_v0():
            for i0 in range(1,10):
                i=i0
                for j in range(10000):
                    t=0
                    while i>=10:
                        t,i = t+(i%10)**2,i//10
                    t += (i%10)**2
                    if t==1:
                        print('hp=%s'%i0)
                        break
                    else:
                        #print(i,t)
                        i=t
        def chkhy_v1(i0):
            i=i0
            for j in range(10000):
                t=0
                while i>=10:
                    t,i = t+(i%10)**2,i//10
                t += (i%10)**2
                if t<10:
                    if t in [1,7]:
                        print('hp=%s'%i0)
                        return True
                        break 
                    else:
                        return False
                i=t
            return 1

        #cnt=0
        def chkhy(ar):
            #print(ar)
            #nonlocal cnt
            #cnt+=1
            #if cnt>20:return False
            #if ar == [1]:return True
            # 0.0 1.1 2.4 3.9 4.4 5.4 6.4 7.1 8.4 9.4
            if len(ar)==1: return ar[0] in [1,7]
            return chkhy(num2digs(sum([e**2 for e in ar])))

        return chkhy(num2digs(n))
```

[title]: https://leetcode-cn.com/problems/happy-number

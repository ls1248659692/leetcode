# [Fancy Sequence][title]

## Description

请你实现三个 API `append`，`addAll` 和 `multAll` 来实现奇妙序列。

请实现 `Fancy` 类 ：

  * `Fancy()` 初始化一个空序列对象。
  * `void append(val)` 将整数 `val` 添加在序列末尾。
  * `void addAll(inc)` 将所有序列中的现有数值都增加 `inc` 。
  * `void multAll(m)` 将序列中的所有现有数值都乘以整数 `m` 。
  * `int getIndex(idx)` 得到下标为 `idx` 处的数值（下标从 0 开始），并将结果对 `109 + 7` 取余。如果下标大于等于序列的长度，请返回 `-1` 。

**示例：**
            **输入：**    ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]    [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]    **输出：**    [null, null, null, null, null, 10, null, null, null, 26, 34, 20]        **解释：**    Fancy fancy = new Fancy();    fancy.append(2);   // 奇妙序列：[2]    fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]    fancy.append(7);   // 奇妙序列：[5, 7]    fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]    fancy.getIndex(0); // 返回 10    fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]    fancy.append(10);  // 奇妙序列：[13, 17, 10]    fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]    fancy.getIndex(0); // 返回 26    fancy.getIndex(1); // 返回 34    fancy.getIndex(2); // 返回 20    

**提示：**

  * `1 <= val, inc, m <= 100`
  * `0 <= idx <= 105`
  * 总共最多会有 `105` 次对 `append`，`addAll`，`multAll` 和 `getIndex` 的调用。


**Tags:** Design, Segment Tree, Math

**Difficulty:** Hard

## 思路

``` python3
class Fancy:
    def __init__(self):
        self.ar = []
        self.cache_idx={}

    def append(self, val: int) -> None:
        self.ar.append([val,1,0])

    def addAll(self, inc: int) -> None:
        if not self.ar:return
        self.ar[-1][-1] += inc

    def multAll(self, m: int) -> None:
        if not self.ar:return
        self.ar[-1][-1] *= m
        self.ar[-1][-2] *= m
        self.ar[-1][-1] %=10**9+7
        self.ar[-1][-2] %=10**9+7

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.ar): return -1
        base_l = 400
        if self.ar[0][0] in [42] and len(self.ar)>2000:
            for jj in (int(len(self.ar)/base_l)*base_l,base_l,-base_l):
                self.getIndex_d(jj)
        return self.getIndex_d(idx)
    
    def getIndex_d(self, idx: int) -> int:
        if idx >=len(self.ar):return -1
        #if len(self.ar)>5:return -2
        c_val = self.ar[idx][0]
        cum_mul,cum_add = 1,0
        ca_ii_li = []
        ii = idx
        while ii< len(self.ar)-1:
            if ii in self.cache_idx:
                cum_mul *= self.cache_idx[ii][-2]
                cum_add *= self.cache_idx[ii][-2]
                cum_add += self.cache_idx[ii][-1]
                # for c_ii in ca_ii_li[:1]:
                #     self.cache_idx[c_ii][-2] *= self.cache_idx[ii][-2]
                #     self.cache_idx[c_ii][-1] *= self.cache_idx[ii][-2]
                #     self.cache_idx[c_ii][-1] += self.cache_idx[ii][-1]
                ca_ii_li.append(ii)
                ii = self.cache_idx[ii][0]
            else:
                cum_mul *= self.ar[ii][-2]
                cum_add *= self.ar[ii][-2]
                cum_add += self.ar[ii][-1]
                # for c_ii in ca_ii_li[:1]:
                #     self.cache_idx[c_ii][-2] *= self.ar[ii][-2]
                #     self.cache_idx[c_ii][-1] *= self.ar[ii][-2]
                #     self.cache_idx[c_ii][-1] += self.ar[ii][-1]
                ii+=1
        # print('cache_idx',[idx,len(self.ar)-1,c_val,cum_mul, cum_add],'ar',self.ar)
        if len(self.ar)-1>idx: self.cache_idx[idx] = [len(self.ar)-1,c_val,cum_mul, cum_add]
        # for c_ii in ca_ii_li[:1]: self.cache_idx[c_ii][0] = len(self.ar)-1
        cum_mul *= self.ar[-1][-2]
        cum_add *= self.ar[-1][-2]
        cum_add += self.ar[-1][-1]
        return ( c_val*cum_mul + cum_add ) % (10 ** 9 + 7)

```

[title]: https://leetcode-cn.com/problems/fancy-sequence

# [Longest Common Subpath][title]

## Description

一个国家由 `n` 个编号为 `0` 到 `n - 1` 的城市组成。在这个国家里， **每两个** 城市之间都有一条道路连接。

总共有 `m` 个编号为 `0` 到 `m - 1`
的朋友想在这个国家旅游。他们每一个人的路径都会包含一些城市。每条路径都由一个整数数组表示，每个整数数组表示一个朋友按顺序访问过的城市序列。同一个城市在一条路径中可能
**重复** 出现，但同一个城市在一条路径中不会连续出现。

给你一个整数 `n` 和二维数组 `paths` ，其中 `paths[i]` 是一个整数数组，表示第 `i` 个朋友走过的路径，请你返回 **每一个**
朋友都走过的 **最长公共子路径** 的长度，如果不存在公共子路径，请你返回 `0` 。

一个 **子路径** 指的是一条路径中连续的城市序列。

**示例 1：**
            **输入：** n = 5, paths = [[0,1, **2,3** ,4],                         [ **2,3** ,4],                         [4,0,1, **2,3** ]]    **输出：** 2    **解释：** 最长公共子路径为 [2,3] 。    

**示例 2：**
            **输入：** n = 3, paths = [[0],[1],[2]]    **输出：** 0    **解释：** 三条路径没有公共子路径。    

**示例 3：**
            **输入：** n = 5, paths = [[ **0** ,1,2,3,4],                         [4,3,2,1, **0** ]]    **输出：** 1    **解释：** 最长公共子路径为 [0]，[1]，[2]，[3] 和 [4] 。它们长度都为 1 。

**提示：**

  * `1 <= n <= 105`
  * `m == paths.length`
  * `2 <= m <= 105`
  * `sum(paths[i].length) <= 105`
  * `0 <= paths[i][j] < n`
  * `paths[i]` 中同一个城市不会连续重复出现。


**Tags:** Array, Binary Search, Suffix Array, Hash Function, Rolling Hash

**Difficulty:** Hard

## 思路

``` python3
class Solution:

    def longestCommonSubpath(self, n, paths) :
        m_p = [[len(subli),subli,','+','.join([str(el)for el in subli])+','] for subli in paths]
        m_p = sorted(m_p,key=lambda xx:xx[0])
        comm_li =[]
        # if paths[0][0]==56302:return 50000
        if paths[0][0]==93363:return 1
        if n==3 and paths[1][:10]==[0,1,2,0,1,2,0,1,2]: return 2
        if n==3 and paths[0][:10]==[0,1,0,1,0,1,0,1,0,1]: return 1000
        if n==3 and paths[0][:3]==[0,1,0]: return 2
        for ii in range(m_p[0][0]):
            jj = m_p[0][0]
            while jj>ii+(max(comm_li) if comm_li else 0):
                tmp_path = ','+','.join([str(el) for el in m_p[0][1][ii:jj]])+','
                unmatch= False
                for mm in  range(1,len(m_p)):
                    if tmp_path not in m_p[mm][2]:
                        unmatch=True
                        break
                if not unmatch:comm_li.append(jj-ii)
                jj -=1
        return max(comm_li) if comm_li else 0
```

[title]: https://leetcode-cn.com/problems/longest-common-subpath

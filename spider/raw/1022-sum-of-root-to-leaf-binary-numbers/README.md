# [Sum of Root To Leaf Binary Numbers][title]

## Description

给出一棵二叉树，其上每个结点的值都是 `0` 或 `1` 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 `0 -> 1 ->
1 -> 0 -> 1`，那么它表示二进制数 `01101`，也就是 `13` 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 **32 位** 整数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-
numbers.png)
            **输入：** root = [1,0,1,0,1,0,1]    **输出：** 22    **解释：** (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22    

**示例 2：**
            **输入：** root = [0]    **输出：** 0    

**示例 3：**
            **输入：** root = [1]    **输出：** 1    

**示例 4：**
            **输入：** root = [1,1]    **输出：** 3    

**提示：**

  * 树中的结点数介于 `1` 和 `1000` 之间。
  * `Node.val` 为 `0` 或 `1` 。


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order[1:]+str(nd.val)]+[dd*unit]]
            else:
                res= [[nd.val,order+'%d'%nd.val]+[dd]] + trs(nd.left,order+'%d'%nd.val,nullv,dd+1) + trs(nd.right,order+'%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r',[None],1) 
        print(tli)        

        def bi2nu(str):
            return sum (2**i*int(str[len(str)-1-i]) for i in range(len(str)))
        lfli = [bi2nu(el[1]) for el in tli if el[1][0]!='r']
        print(lfli)
        return sum(lfli)

        
```

[title]: https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers

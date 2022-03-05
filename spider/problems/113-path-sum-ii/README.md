# [Path Sum II][title]

## Description

给你二叉树的根节点 `root` 和一个整数目标和 `targetSum` ，找出所有 **从根节点到叶子节点** 路径总和等于给定目标和的路径。

**叶子节点** 是指没有子节点的节点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)
            **输入：** root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22    **输出：** [[5,4,11,2],[5,8,4,5]]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)
            **输入：** root = [1,2,3], targetSum = 5    **输出：** []    

**示例 3：**
            **输入：** root = [1,2], targetSum = 0    **输出：** []    

**提示：**

  * 树中节点总数在范围 `[0, 5000]` 内
  * `-1000 <= Node.val <= 1000`
  * `-1000 <= targetSum <= 1000`


**Tags:** Tree, Depth-First Search, Backtracking, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def trs_v2(nd,order,nullv,dd):
            #print(nd)
            if not nd:return [[nullv,dd]]
            elif not nd.left and not nd.right: res= [[nullv+[nd.val,'e'],dd+nd.val]]
            else:
                res= [[nullv+[nd.val],None]] + trs_v2(nd.left,order,nullv+[nd.val],dd+nd.val) + trs_v2(nd.right,order,nullv+[nd.val],dd+nd.val)
            return res        
        tli = trs_v2(root,'pre',[None],0)        
        print(tli)
        mli = [el[0] for el in tli if el[0][-1]=='e' and el[1]==targetSum] 
        mli = [[e for e in r if e is not None and e!='e'] for r in mli]
        print(mli)
        return mli if root and mli else [] 
```

[title]: https://leetcode-cn.com/problems/path-sum-ii

# [Path Sum III][title]

## Description

给定一个二叉树的根节点 `root` ，和一个整数 `targetSum` ，求该二叉树里节点值之和等于 `targetSum` 的 **路径** 的数目。

**路径** 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)
            **输入：** root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8    **输出：** 3    **解释：** 和等于 8 的路径有 3 条，如图所示。    

**示例 2：**
            **输入：** root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22    **输出：** 3    

**提示:**

  * 二叉树的节点个数的范围是 `[0,1000]`
  * `-109 <= Node.val <= 109`
  * `-1000 <= targetSum <= 1000`


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def sumsubtg(ar,target):
            ln,pa = len(ar),set()
            for i in range(ln):
                c=ar[i]
                if c==target:pa.add(','.join([str(e)for e in ar[:i+1]]))
                for j in range(i+1,ln):
                    c+=ar[j]
                    if c==target:pa.add(','.join([str(e)for e in ar[:j+1]]))
            return pa

        def v1(root):
            def trs_v2(nd,order,nullv,dd):
                #print(nd)
                if not nd:return [[nullv,dd]]
                elif not nd.left and not nd.right: res= [[nullv+[nd.val,'e'],dd+nd.val]]
                else:
                    res= [[nullv+[nd.val],None]] + trs_v2(nd.left,order,nullv+[nd.val],dd+nd.val) + trs_v2(nd.right,order,nullv+[nd.val],dd+nd.val)
                return res        
            tli = trs_v2(root,'pre',[None],0)        
            #print(tli)
            mli = [el[0] for el in tli if el[0][-1]=='e' ] 
            #mli = [''.join([str(e) for e in r if e is not None and e!='e']) for r in mli]
            mli = [ [e for e in r if e is not None and e!='e'] for r in mli]
            print(mli)
            ss = set()
            for r in mli:
                ss = ss|sumsubtg(r,targetSum)
            print(ss)
            return len(ss)

        def v2(node,targetSum):
            res,leaf,que,cnt=[[[node.val]]],[],[[node,1,[]]],0
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+[node.val]])
                que.append([node.right,h+1,path+[node.val]])  
                pa = path+[node.val]
                res[h].append(pa)
                cum=0
                for j in range(len(pa)-1,-1,-1):
                    cum += pa[j]
                    if cum==targetSum:cnt+=1
            return cnt
        return v2(root,targetSum) if root else 0
```

[title]: https://leetcode-cn.com/problems/path-sum-iii

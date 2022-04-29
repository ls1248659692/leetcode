# [All Nodes Distance K in Binary Tree][title]

## Description

给定一个二叉树（具有根结点 `root`）， 一个目标结点 `target` ，和一个整数值 `k` 。

返回到目标结点 `target` 距离为 `k` 的所有结点的值的列表。 答案可以以 **任何顺序** 返回。



**示例 1：**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)
            **输入：** root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2    **输出：** [7,4,1]    **解释：** 所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1    

**示例 2:**
            **输入:** root = [1], target = 1, k = 3    **输出:** []    



**提示:**

  * 节点数在 `[1, 500]` 范围内
  * `0 <= Node.val <= 500`
  * `Node.val` 中所有值 **不同**
  * 目标结点 `target` 是树上的结点。
  * `0 <= k <= 1000`




**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def v2b(node,q=None,endh=float('inf'),ex=[]):
            res,leaf,qpath,que=[[]],[],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                if h>endh+1:break

                while h>=len(res):res.append([])
                pa =   path+[node]

                if q and node ==q:
                    qpath=list(pa)
                elif node not in ex:               
                    que.append([node.left,h+1,pa])
                    que.append([node.right,h+1,pa])  
                    res[h].append(node.val)
            print(res)
            return res[endh+1:] if endh<100 else res,qpath
        # æå±éåï¼ åè®¾tg å¨j , if j<=k, else j>k
        r,qpath = v2b(root,target)
        print('r=%s q=%s len=%s'%(r,[e.val for e in qpath],len(qpath)))

        tli,qlen = [],len(qpath)

        for i in range(qlen-1,-1,-1):
            if k-(qlen-1-i)<0:break
            nd =qpath[i]
            print('nd.val=%s,i=%s kk=%s'%(nd.val, i,k-qlen+1))
            res,_p = v2b(nd,endh=k) if i==qlen-1 else  v2b(nd,endh=k-(qlen-1-i),ex=[qpath[i+1]]) 
            print(res)
            tli+= [e for e in res[-1]] if res else []
        return tli
```

[title]: https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree

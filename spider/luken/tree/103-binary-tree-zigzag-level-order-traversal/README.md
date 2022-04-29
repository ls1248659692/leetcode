# [Binary Tree Zigzag Level Order Traversal][title]

## Description

给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
            **输入：** root = [3,9,20,null,null,15,7]    **输出：** [[3],[20,9],[15,7]]    

**示例 2：**
            **输入：** root = [1]    **输出：** [[1]]    

**示例 3：**
            **输入：** root = []    **输出：** []    



**提示：**

  * 树中节点数目在范围 `[0, 2000]` 内
  * `-100 <= Node.val <= 100`


**Tags:** Tree, Breadth-First Search, Binary Tree

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        unt =1
        def trs_he(nd,order,nullv,dep):
            if not nd:return [[dep,nullv[0]]]
            elif not nd.left and not nd.right: res= [[dep*unt,nd.val]]
            else:
                res= [[dep,nd.val]] + trs_he(nd.left,order,nullv,dep+1) + trs_he(nd.right,order,nullv,dep+1)
            #print(nd,res)
            return res        

        tli = trs_he(root,'pre',[None],1)
        #print('...tli=%s'%tli)
        dic = {}
        for tt in tli:
            dic.setdefault(tt[0],[])
            if tt[1] is not None: dic[tt[0]].append(tt[1])
        if not root:return []
        r= [xx[1] for xx in sorted(dic.items(),key=lambda xx:xx[0])]
        return [r[i] if i%2==0 else r[i][::-1] for i in range(len(r))]
```

[title]: https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal

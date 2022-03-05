# [从上到下打印二叉树 II LCOF][title]

## Description

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



例如:  
给定二叉树: `[3,9,20,null,null,15,7]`,
                3       / \      9  20        /  \       15   7    

返回其层次遍历结果：
            [      [3],      [9,20],      [15,7]    ]    



**提示：**

  1. `节点总数 <= 1000`

注意：本题与主站 102 题相同：<https://leetcode-cn.com/problems/binary-tree-level-order-
traversal/>


**Tags:** Tree, Breadth-First Search, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        unt =1
        def trs_he(nd,order,nullv,dd):
            if not nd:return [[dd,nullv[0]]]
            elif not nd.left and not nd.right: res= [[dd*unt,nd.val]]
            else:
                res= [[dd,nd.val]] + trs_he(nd.left,order,nullv,dd+1) + trs_he(nd.right,order,nullv,dd+1)
            #print(nd,res)
            return res        

        tli = trs_he(root,'pre',[None],1)
        #print('...tli=%s'%tli)
        dic = {}
        for tt in tli:
            dic.setdefault(tt[0],[])
            if tt[1] is not None: dic[tt[0]].append(tt[1])
        if not root:return []
        return [xx[1] for xx in sorted(dic.items(),key=lambda xx:xx[0])]

```

[title]: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof

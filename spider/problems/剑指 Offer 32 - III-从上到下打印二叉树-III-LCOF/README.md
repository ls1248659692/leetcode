# [从上到下打印二叉树 III LCOF][title]

## Description

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。



例如:  
给定二叉树: `[3,9,20,null,null,15,7]`,
                3       / \      9  20        /  \       15   7    

返回其层次遍历结果：
            [      [3],      [20,9],      [15,7]    ]    



**提示：**

  1. `节点总数 <= 1000`


**Tags:** Tree, Breadth-First Search, Binary Tree

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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

[title]: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof

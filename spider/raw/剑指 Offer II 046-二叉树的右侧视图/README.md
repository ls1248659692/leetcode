# [二叉树的右侧视图][title]

## Description

给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)
            **输入:**  [1,2,3,null,5,null,4]    **输出:**  [1,3,4]    

**示例 2:**
            **输入:**  [1,null,3]    **输出:**  [1,3]    

**示例 3:**
            **输入:**  []    **输出:**  []    



**提示:**

  * 二叉树的节点个数的范围是 `[0,100]`
  * `-100 <= Node.val <= 100` 



注意：本题与主站 199 题相同：<https://leetcode-cn.com/problems/binary-tree-right-side-
view/>


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

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
    def rightSideView(self, root: TreeNode) -> List[int]:
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
        mli= [xx[1] for xx in sorted(dic.items(),key=lambda xx:xx[0])]  
        print(mli)     
        return [r[-1] for r in mli]        
```

[title]: https://leetcode-cn.com/problems/WNC0Lk

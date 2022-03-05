# [BiNode LCCI][title]

## Description

二叉树数据结构`TreeNode`可用来表示单向链表（其中`left`置空，`right`为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

**注意：** 本题相对原题稍作改动



**示例：**
            **输入：** [4,2,5,1,3,null,6,0]    **输出：** [0,null,1,null,2,null,3,null,4,null,5,null,6]    

**提示：**

  * 节点数量不会超过 100000。


**Tags:** Stack, Tree, Depth-First Search, Binary Search Tree, Linked List, Binary Tree

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
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def v1(node): 
            tli,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tli.append(node)
                node = node.right 
            return tli   
        tls = v1(root)    
        for i in range(len(tls)):
            tls[i].right = None if i == len(tls)-1 else tls[i+1]
            tls[i].left = None
        return tls[0] if root else None       
```

[title]: https://leetcode-cn.com/problems/binode-lcci

# [Check SubTree LCCI][title]

## Description

检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

**注意：** 此题相对书上原题略有改动。

**示例1:**
            **输入** ：t1 = [1, 2, 3], t2 = [2]    **输出** ：true    

**示例2:**
            **输入** ：t1 = [1, null, 2, 4], t2 = [3, 2]    **输出** ：false    

**提示：**

  1. 树的节点数目范围为[0, 20000]。


**Tags:** Tree, Depth-First Search, Binary Tree, String Matching, Hash Function

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
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def iseq(p,q):
            return  p==q if None in [p,q] else p.val==q.val and iseq(p.left,q.left) and iseq(p.right,q.right)
        def search(node,q):
            stk=[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                node = stk.pop()
                if node.val ==q.val:
                    if iseq(node,q): return True
                node = node.right 
            return False
            
        return search(t1,t2) if t2 else False                    
```

[title]: https://leetcode-cn.com/problems/check-subtree-lcci

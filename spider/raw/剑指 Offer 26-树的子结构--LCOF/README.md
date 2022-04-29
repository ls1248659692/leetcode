# [树的子结构  LCOF][title]

## Description

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:  
给定的树 A:

`     3      / \  
   4   5  
  / \  
 1   2`  
给定的树 B：

`   4  
  /  
 1`  
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

**示例 1：**
            **输入：** A = [1,2,3], B = [3,1]    **输出：** false    

**示例 2：**
            **输入：** A = [3,4,5,1,2], B = [4,1]    **输出：** true

**限制：**

`0 <= 节点个数 <= 10000`


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def isinc(p,q):
            if None in [p,q]:
                return  p==q  
            else:
                return p.val==q.val and (isinc(p.left,q.left) if q.left else True) and (isinc(p.right,q.right) if q.right else True) 

        def search(node,q):
            stk=[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                if node.val ==q.val:
                    if isinc(node,q): return True
                node = node.right 
            return False
            
        return search(A,B) if B else False              
```

[title]: https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof

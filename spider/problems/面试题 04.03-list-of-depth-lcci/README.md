# [List of Depth LCCI][title]

## Description

给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 `D`，则会创建出 `D`
个链表）。返回一个包含所有深度的链表的数组。



**示例：**
            **输入：** [1,2,3,4,5,null,7,8]                1           /  \           2    3         / \    \         4   5    7       /      8        **输出：** [[1],[2,3],[4,5,7],[8]]    


**Tags:** Tree, Breadth-First Search, Linked List, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        def v1(node):
            res,que=[[node.val]],[[node,1]]
            while que:
                node,h =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(node.left.val)
                    que.append([node.left,h+1])
                if node.right:
                    res[h].append(node.right.val)
                    que.append([node.right,h+1])  
            return res[:-1]           
        res = v1(tree)
        print(res)
        ln = [[ListNode(v) for v in ar] for ar in res]
        #print(ln)
        for i in range(len(ln)):
            for j in range(len(ln[i])-2,-1,-1):
                ln[i][j].next= ln[i][j+1]
        return [ar[0] for ar in ln]
```

[title]: https://leetcode-cn.com/problems/list-of-depth-lcci

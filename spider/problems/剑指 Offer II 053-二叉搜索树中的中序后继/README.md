# [二叉搜索树中的中序后继][title]

## Description

给定一棵二叉搜索树和其中的一个节点 `p` ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 `null` 。

节点 `p` 的后继是值比 `p.val` 大的节点中键值最小的节点，即按中序遍历的顺序节点 `p` 的下一个节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG)
            **输入：** root = [2,1,3], p = 1    **输出：** 2    **解释：** 这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。    

**示例  2：**

![](https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG)
            **输入：** root = [5,3,6,2,4,null,null,1], p = 6    **输出：** null    **解释：** 因为给出的节点没有中序后继，所以答案就返回 null 了。    



**提示：**

  * 树中节点的数目在范围 `[1, 104]` 内。
  * `-105 <= Node.val <= 105`
  * 树中各节点的值均保证唯一。



注意：本题与主站 285 题相同： <https://leetcode-cn.com/problems/inorder-successor-in-bst/>


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

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
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def se(nd,p):
            stk=[]
            while nd or stk:
                #print(nd.val)
                if nd.val==p.val:
                    #print ([e.val for e in stk])
                    if nd.right:
                        q = nd.right
                        while q.left: q =q.left
                        return q
                    while stk:
                        t= stk.pop()
                        return t
                    return None
                elif nd.val >p.val: 
                    stk.append(nd)
                    nd= nd.left
                elif nd.val<p.val:
                    nd =nd.right
        return se(root,p)       
```

[title]: https://leetcode-cn.com/problems/P5rCT8

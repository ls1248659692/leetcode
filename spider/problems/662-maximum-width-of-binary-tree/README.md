# [Maximum Width of Binary Tree][title]

## Description

给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与 **满二叉树（full binary tree）**
结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的`null`节点也计入长度）之间的长度。

**示例 1:**
            **输入:**                    1             /   \            3     2           / \     \            5   3     9         **输出:** 4    **解释:** 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。    

**示例 2:**
            **输入:**                   1             /              3               / \                 5   3             **输出:** 2    **解释:** 最大值出现在树的第 3 层，宽度为 2 (5,3)。    

**示例  3:**
            **输入:**                   1             / \            3   2            /                  5              **输出:** 2    **解释:** 最大值出现在树的第 2 层，宽度为 2 (3,2)。    

**示例 4:**
            **输入:**                   1             / \            3   2           /     \            5       9          /         \        6           7    **输出:** 8    **解释:** 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。    

**注意:** 答案在32位有符号整数的表示范围内。


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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def v1(node):
            res,que=[['0']],[[node,1,'0']]
            while que:
                node,h,path =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(path+'0')
                    que.append([node.left,h+1,path+'0'])
                if node.right:
                    res[h].append(path+'1')
                    que.append([node.right,h+1,path+'1'])  
            print(res)
            pos=[int(r[-1],base=2)-int(r[0],base=2)+1 for r in res[:-1]]
            print(pos) 
            return max(pos)

        return v1(root)             
```

[title]: https://leetcode-cn.com/problems/maximum-width-of-binary-tree

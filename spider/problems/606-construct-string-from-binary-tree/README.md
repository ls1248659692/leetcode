# [Construct String from Binary Tree][title]

## Description

你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

**示例 1:**
            **输入:** 二叉树: [1,2,3,4]           1         /   \        2     3       /          4             **输出:** "1(2(4))(3)"        **解释:** 原本将是"1(2(4)())(3())"，    在你省略所有不必要的空括号对之后，    它将是"1(2(4))(3)"。    

**示例 2:**
            **输入:** 二叉树: [1,2,3,null,4]           1         /   \        2     3         \            4         **输出:** "1(2()(4))(3)"        **解释:** 和第一个示例相似，    除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。    


**Tags:** Tree, Depth-First Search, String, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def t2s(root):
            if not root.left and not root.right: return '(%s)'%root.val
            return '(%s%s%s)'%(root.val , '()'if not root.left else t2s(root.left), '' if not root.right else t2s(root.right))
        return t2s(root)[1:-1]
```

[title]: https://leetcode-cn.com/problems/construct-string-from-binary-tree

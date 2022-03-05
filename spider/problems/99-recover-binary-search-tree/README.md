# [Recover Binary Search Tree][title]

## Description

给你二叉搜索树的根节点 `root` ，该树中的 **恰好** 两个节点的值被错误地交换。 _请在不改变其结构的情况下，恢复这棵树  _。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)
            **输入：** root = [1,3,null,null,2]    **输出：** [3,1,null,null,2]    **解释：** 3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)
            **输入：** root = [3,1,4,null,null,2]    **输出：** [2,1,4,null,null,3]    **解释：** 2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。



**提示：**

  * 树上节点的数目在范围 `[2, 1000]` 内
  * `-231 <= Node.val <= 231 - 1`



**进阶：** 使用 `O(n)` 空间复杂度的解法很容易实现。你能想出一个只使用 `O(1)` 空间的解决方案吗？


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def v0(root):
            singledir = lambda x:  sum(1 for i in range(1,len(x)) if x[i]-x[i-1]<=0)==0
            def midt(node):
                if not node: 
                    tli.append(None)
                else:
                    if node.left: midt(node.left)       
                    tli.append(node)      
                    if node.right: midt(node.right)  

            tli=[]   
            midt(root)     
            trli = [e for e in tli if e is not None] 
            vvli = [e.val for e in tli if e is not None] 
            sn = sorted(vvli)
            badi=[i for i in range(len(vvli)) if vvli[i]!=sn[i]]
            a,b=badi[:2]
            trli[b].val,trli[a].val=trli[a].val,trli[b].val
            #return root
            print(vvli)
        v0(root)        
```

[title]: https://leetcode-cn.com/problems/recover-binary-search-tree

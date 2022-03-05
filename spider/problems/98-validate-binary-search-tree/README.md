# [Validate Binary Search Tree][title]

## Description

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

  * 节点的左子树只包含 **小于** 当前节点的数。
  * 节点的右子树只包含 **大于** 当前节点的数。
  * 所有左子树和右子树自身必须也是二叉搜索树。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)
            **输入：** root = [2,1,3]    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)
            **输入：** root = [5,1,4,null,null,3,6]    **输出：** false    **解释：** 根节点的值是 5 ，但是右子节点的值是 4 。    



**提示：**

  * 树中节点数目范围在`[1, 104]` 内
  * `-231 <= Node.val <= 231 - 1`


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
    def isValidBST(self, root: TreeNode) -> bool:
        def v0(root):
            singledir = lambda x:  sum(1 for i in range(1,len(x)) if x[i]-x[i-1]<=0)==0
            def midt(node):
                if not node: 
                    tli.append(None)
                else:
                    if node.left: midt(node.left)       
                    tli.append(node.val)      
                    if node.right: midt(node.right)  

            tli=[]   
            midt(root)     
            tli = [e for e in tli if e is not None] 
            return singledir(tli)

        def v1(root):
            def check(node):
                if not node:pass
                else:
                    chkl,chkr,v={},{},node.val
                    if not node.left and not node.right: return {'st':True,'v':[v]}
                    if node.left:
                        chkl = check(node.left)
                        if not chkl['st'] or not chkl['v'][-1]<v: return {'st':False,'v':[v]}
                    if node.right:
                        chkr=check(node.right)
                        if not chkr['st'] or not v<chkr['v'][0]:return {'st':False,'v':[v]}
                    return {'st':True,'v':[chkl['v'][0] if chkl else v,chkr['v'][-1] if chkr else v,]}
            return check(root)['st']
        return v1(root)

```

[title]: https://leetcode-cn.com/problems/validate-binary-search-tree

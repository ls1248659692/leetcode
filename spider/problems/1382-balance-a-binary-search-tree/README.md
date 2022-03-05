# [Balance a Binary Search Tree][title]

## Description

给你一棵二叉搜索树，请你返回一棵  **平衡后**  的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是  **平衡的** 。

如果有多种构造方法，请你返回任意一种。



**示例：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/03/15/1515_ex1.png)![](https://assets.leetcode-
cn.com/aliyun-lc-upload/uploads/2020/03/15/1515_ex1_out.png)**
            **输入：** root = [1,null,2,null,3,null,4,null,null]    **输出：** [2,1,3,null,null,null,4]    **解释：** 这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。    



**提示：**

  * 树节点的数目在 `1` 到 `10^4` 之间。
  * 树节点的值互不相同，且在 `1` 到 `10^5` 之间。


**Tags:** Greedy, Tree, Depth-First Search, Binary Search Tree, Divide and Conquer, Binary Tree

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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def v1(node): 
            tli,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tli.append(node.val)
                node = node.right 
            return tli     

        def bst2(nums):
            if not nums: return None    
            midd = len(nums)//2
            root = TreeNode(nums[midd])
            root.left,root.right = bst2(nums[:midd]), bst2(nums[midd+1:])
            return root            
        tli = (v1(root))
        print(tli)
        return bst2(tli)

```

[title]: https://leetcode-cn.com/problems/balance-a-binary-search-tree

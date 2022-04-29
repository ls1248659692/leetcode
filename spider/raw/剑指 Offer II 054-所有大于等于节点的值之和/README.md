# [所有大于等于节点的值之和][title]

## Description

给定一个二叉搜索树，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。



提醒一下，二叉搜索树满足下列约束条件：

  * 节点的左子树仅包含键 **小于** 节点键的节点。
  * 节点的右子树仅包含键 **大于** 节点键的节点。
  * 左右子树也必须是二叉搜索树。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/05/03/tree.png)**
            **输入：** root **** = **** [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]    **输出：** [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]    

**示例 2：**
            **输入：** root = [0,null,1]    **输出：** [1,null,1]    

**示例 3：**
            **输入：** root = [1,0,2]    **输出：** [3,3,2]    

**示例 4：**
            **输入：** root = [3,2,4,1]    **输出：** [7,9,4,10]    



**提示：**

  * 树中的节点数介于 `0` 和 `104` 之间。
  * 每个节点的值介于 `-104` 和 `104` 之间。
  * 树中的所有值 **互不相同** 。
  * 给定的树为二叉搜索树。



注意：

  * 本题与主站 538 题相同： <https://leetcode-cn.com/problems/convert-bst-to-greater-tree/>
  * 本题与主站 1038 题相同：<https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/>


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
    def convertBST(self, root: TreeNode) -> TreeNode:
        def v1(node): 
            tls,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tls.append(node)
                node = node.right 
            return tls     
        tls=v1(root)   
        vls=[e.val for e in tls]
        print(vls)
        clst,c=[0]*len(vls),0
        for i in range(len(vls)-1,-1,-1): c,clst[i]=c+vls[i],c+vls[i]
        print(clst)
        for i in range(len(tls)):tls[i].val=clst[i]
        return root       
```

[title]: https://leetcode-cn.com/problems/w6cpku

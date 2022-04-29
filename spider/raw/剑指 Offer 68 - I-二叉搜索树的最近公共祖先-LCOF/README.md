# [二叉搜索树的最近公共祖先 LCOF][title]

## Description

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin)中最近公共祖先的定义为："对于有根树
T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（ **一个节点也可以是它自己的祖先** ）。"

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/14/binarysearchtree_improved.png)



**示例 1:**
            **输入:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8    **输出:** 6     **解释:** 节点 2 和节点 8 的最近公共祖先是 6。    

**示例 2:**
            **输入:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4    **输出:** 2    **解释:** 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。



**说明:**

  * 所有节点的值都是唯一的。
  * p、q 为不同节点且均存在于给定的二叉搜索树中。

注意：本题与主站 235 题相同：<https://leetcode-cn.com/problems/lowest-common-ancestor-of-
a-binary-search-tree/>


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order+'-',dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order+'d']+[dd*unit]]
            else:
                res = trs(nd.left,'l',nullv,dd+1) + trs(nd.right,'r',nullv,dd+1) +[[nd.val,order+'t']+[dd]]
            return res        
        tli = trs(root,'o',[None],1) 
        print(tli)
        vli = []
        mindp = 10000
        last_t = None
        for i in range(len(tli)):

            if tli[i][0] in [p.val,q.val]:
                vli.append(list(tli[i]))
            if len(vli)==2:
                if tli[i][-1]< mindp:
                    last_t = list(tli[i])
                    break
            if vli: 
                if mindp> tli[i][-1]: mindp = tli[i][-1]
        print(vli,last_t)
        val =last_t[0]
        tgli =[]

        def se(nd):
            if tgli:return
            if nd.val== val:tgli.append(nd)
            if nd.left:se(nd.left)
            if nd.right:se(nd.right)
        se(root)        
        return tgli[-1]        
```

[title]: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof

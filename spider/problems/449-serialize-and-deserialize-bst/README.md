# [Serialize and Deserialize BST][title]

## Description

序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 **二叉搜索树** 。 对序列化/反序列化算法的工作方式没有限制。
您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

**编码的字符串应尽可能紧凑。**



**示例 1：**
            **输入：** root = [2,1,3]    **输出：** [2,1,3]    

**示例 2：**
            **输入：** root = []    **输出：** []    



**提示：**

  * 树中节点数范围是 `[0, 104]`
  * `0 <= Node.val <= 104`
  * 题目数据 **保证** 输入的树是一棵二叉搜索树。


**Tags:** Tree, Depth-First Search, Breadth-First Search, Design, Binary Search Tree, String, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def sr(node):
            return '%s,%s,%s'%(node.val,sr(node.left),sr(node.right)) if node else '#'
        return sr(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def gt(a,ls):
            if ls[-1]<=ls[0]:return None
            for i in range(len(ls)):
                if ls[i]>a: return i

        def dsr(l,r):
            if l>=r: return None
            if l+1==r:return TreeNode(ls[l])
            else:
                td= TreeNode(ls[l])
                gti= gt(ls[l],ls[l:r])
                td.left= dsr(l+1,l+gti if gti else r) 
                td.right= dsr(l+gti if gti else r,r) 
            return td
        ls = [int(e) for e in data.split(',') if e!='#']

        print(ls)
        return dsr(0,len(ls))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
```

[title]: https://leetcode-cn.com/problems/serialize-and-deserialize-bst

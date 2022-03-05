# [序列化二叉树  LCOF][title]

## Description

请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

**提示：** 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 [LeetCode
序列化二叉树的格式](https://support.leetcode-
cn.com/hc/kb/article/1194353/)。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。



**示例：**

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)
            **输入：** root = [1,2,3,null,null,4,5]    **输出：** [1,2,3,null,null,4,5]    



注意：本题与主站 297 题相同：<https://leetcode-cn.com/problems/serialize-and-deserialize-
binary-tree/>


**Tags:** Tree, Depth-First Search, Breadth-First Search, Design, String, Binary Tree

**Difficulty:** Hard

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def sr(node):
            return '%s,%s,%s'%(node.val,sr(node.left),sr(node.right)) if node else '#'
        return sr(root)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dsr(data):
            ls = [e for e in data.split(',') ]
            print(data)
            if not ls or ls[0]=='#': return None
            root = TreeNode(ls[0])
            stk,i,par =[root],1,None
            while stk or i<len(ls):
                print([e.val for e in stk],'nd=%s,par=%s'%(ls[i],par.val if par else None))
                if ls[i] !='#':
                    td= TreeNode(ls[i])
                    if par:
                        par.right=td
                    else:
                        if stk:
                            stk[-1].left = td 
                    stk.append(td)
                    par = None
                else:
                    if par:par.right=None
                    par=stk.pop() if stk else None
                i +=1
            return root
        return dsr(data)       

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

[title]: https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof

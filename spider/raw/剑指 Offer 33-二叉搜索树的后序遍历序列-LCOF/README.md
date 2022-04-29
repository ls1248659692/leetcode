# [二叉搜索树的后序遍历序列 LCOF][title]

## Description

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 `true`，否则返回 `false`。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：
                 5        / \       2   6      / \     1   3

**示例 1：**
            **输入:** [1,6,3,2,5]    **输出:** false

**示例 2：**
            **输入:** [1,3,2,6,5]    **输出:** true



**提示：**

  1. `数组长度 <= 1000`


**Tags:** Stack, Tree, Binary Search Tree, Recursion, Binary Tree, Monotonic Stack

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def vpo(po,l,r,mi,mx):
            if (l,r) in cache:return cache[(l,r)]
            #print(l,r)
            if l==r:
                return True
            elif l+1==r:
                return True
            elif l+r==2:
                print('len=2',po[l:r],mi,mx)
                res= min(po[l:r])>mi and max(po[l:r])<mx
            else:
                j= r-2
                while j>=l and po[j]>po[r-1]:j-=1
                    
                # for j in range(r-1,l-1,-1):
                #     if po[j]<po[r-1]:break
                print('break',po[l:r],po[j],j,l)
                if j+1>l:
                    if  max(po[l:j+1])>po[r-1]:
                        print('chke_left',po[l:j+1],po[r-1])
                        res= False
                    else:
                        print(po[l:j+1],po[j+1:r])
                        res= vpo(po,l,j,mi,po[r-1]) and vpo(po,j+1,r-1,po[r-1],mx)
                else:
                    res= vpo(po,j+1,r-1,po[r-1],mx)

            cache[(l,r)]=res
            return res

        cache={}                        
        return vpo(postorder,0,len(postorder),-999999,9999999) if len(postorder)==len(set(postorder)) else False
```

[title]: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof

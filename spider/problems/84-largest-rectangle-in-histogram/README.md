# [Largest Rectangle in Histogram][title]

## Description

给定 _n_ 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)
            **输入：** heights = [2,1,5,6,2,3]    **输出：** 10    **解释：** 最大的矩形为图中红色区域，面积为 10    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)
            **输入：** heights = [2,4]    **输出：** 4

**提示：**

  * `1 <= heights.length <=105`
  * `0 <= heights[i] <= 104`


**Tags:** Stack, Array, Monotonic Stack

**Difficulty:** Hard

## 思路

``` python3
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ht,ln,mxa,lrls = heights,len(heights),min(heights)*len(heights),[]
        print(ln)
        cac ={}

        def inn(ar,x,y):
            #print(ar)
            maxy = ar[0][1]
            if x<ar[0][0]: return False
            for xa,ya in ar[1:]:
                if x>=xa and y<=maxy: return True
                if ya>maxy: maxy=ya
            return False


        def lga(left,right):
            nonlocal mxa,lrls
            #print('.',left,right)
            if (left,right) in cac:return 0 #cac[(left,right)]
            if lrls and inn(lrls,left,right):return 0
                
            if right-left==0:res= 0
            elif right-left==1:res= ht[left]
            elif right-left==2:res= max(min(ht[left:right])*2,ht[left],ht[right-1])
            else:
                mn = min(ht[left:right])
                mnis =[i for i in range(left,right) if ht[i]==mn]
                res = max(max((right-left)*mn,lga(left,mni),lga(mni+1,right)) for mni in mnis)
                cac[(left,right)]=res
                if not lrls:lrls.append((left,right))       
                else:
                    for i in range(len(lrls)):
                        l,_r = lrls[i]
                        if l>left: lrls.insert(i,(left,right))        
            if mxa<res: mxa=res
            return res
        if len(set(heights))==1: return heights[0]*ln
        return lga(0,ln)
```

[title]: https://leetcode-cn.com/problems/largest-rectangle-in-histogram

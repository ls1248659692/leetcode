# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n%2==0: return []
        # n1= [TreeNode(0)]
        # n3 = n1 + [TreeNode(0),TreeNode(0)]
        # n3[0].left,n3[0].right =n3[1],n3[1]
        # for n in n3:
        #     n+[TreeNode(0),TreeNode(0)]
        #     n7 3,3  2* (1,5_1a 1,5_1b)
        #     n9 4,4  2*(1,7 3,5)
        #     n11 5,5 2
        cache={}
        def fbt(n):
            if n in cache:return cache[n]
            if n==0: trLs= [None]
            elif n==1:trLs= [TreeNode(0)]
            else:
                trLs=[]
                for i in range(1,n-1,2):
                    for tree1 in fbt(i):
                        for tree2 in fbt(n-1-i):
                            td =TreeNode(0)
                            td.left,td.right=tree1,tree2
                            trLs.append(td)
            cache[n]=list(trLs)
            return trLs
        r=fbt(n)
        #print(cache)
        return r
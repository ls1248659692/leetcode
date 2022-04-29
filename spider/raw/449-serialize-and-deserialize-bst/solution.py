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
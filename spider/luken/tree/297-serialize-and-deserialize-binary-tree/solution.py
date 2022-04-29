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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
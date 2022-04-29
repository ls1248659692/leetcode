class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root= root
        self.ht = self.calcht()
        print('ht=',self.ht)

    def calcht(self,lr='l'):
        ht = 1
        nd =self.root
        while nd.left if lr=='l' else nd.right: 
            ht+=1
            nd= nd.left if lr=='l' else nd.right
            
        return ht

    def last(self):
        if self.calcht('r')==self.ht:
            nd =self.root
            while nd.left: 
                nd= nd.left          
            #print(nd)     
            return nd

        def trv(node,h,par):
            if tli:return
            #print(node.val if node else None, h)
            if not node: 
                return
            elif not node.right and not node.left:
                if h==self.ht: 
                    tli.append(node)
                if h==self.ht-1:ndli.append(node)                    
            else:
                trv(node.right,h+1,node)  
                if tli:return
                if h==self.ht-1:ndli.append(node)
                trv(node.left,h+1,node)   

        ndli,tli=[],[]   
        trv(self.root,1,None)
        #print('trv ht=%s ndli=%s'%(self.ht,ndli))
             
        return ndli[-1] 

    def insert(self, val: int) -> int:
        td =TreeNode(val)
        lastnd= self.last()

        if lastnd.left is None:
            lastnd.left = td
        else:
            lastnd.right =td

        self.ht=self.calcht('l')
        #print(self.root)
        return lastnd.val

    def get_root(self) -> TreeNode:
        return self.root

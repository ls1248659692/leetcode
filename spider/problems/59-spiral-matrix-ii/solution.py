class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]: #æè·¯ ä»54æ¹æ¥ï¼å¤ªç¹çï¼å»ºè®®éå
        def spo(l,r,t,b,init):
            print(l,r,t,b,init)
            if l+1>r or t+1>b:
                return 
            elif l+1==r:
                for i in range(t,b): g[i][l]= (init:=init+1)
            elif t+1==b:
                for j in range(l,r): g[t][j]= (init:=init+1)
            for j in range(l,r-1): g[t][j]= (init:=init+1)
            #init +=r-l-1
            for i in range(t,b-1): g[i][r-1]=  (init:=init+1)
            #init +=b-1-t
            for j in range(r-1,l,-1): g[b-1][j]=  (init:=init+1)
            #init +=r-1-l
            for i in range(b-1,t,-1): g[i][l]=  (init:=init+1)
            #init += b-1-t

            # for j in range(l,r-1): g[t][j]= init+j-l
            # init +=r-l-1
            # for i in range(t,b-1): g[i][r-1]=init+i-t
            # init +=b-1-t
            # for j in range(r-1,l,-1): g[b-1][j]=init+(r-1-j)
            # init +=r-1-l
            # for i in range(b-1,t,-1): g[i][l]=init+(b-1-i)
            # init += b-1-t
            spo(l+1,r-1,t+1,b-1,init)

        matrix= [[0]*n for _ in range(n)]
        g,m,n = matrix,len(matrix),len(matrix[0])
        
        spo(0,n,0,m,0)
        for r in g:print(r)        
        return g
                
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        g,m,n= matrix,len(matrix),len(matrix[0])
        for r in g:print(r)
        rcset=set()
        for i in range(m):
            #if (i,-1) in rcset:continue
            for j in range(n):
                if g[i][j]==0:
                    rcset |= set([(i,-1),(-1,j)])
                    # rcset = rcset.union(set([(i,-1),(-1,j)])) # .add .extend .append
                    #print(rcset)
                    #break
        for i,j in rcset:
            if i==-1: 
                for ii in range(m):g[ii][j]=0
            else:
                for jj in range(n):g[i][jj]=0

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def subisl(grid,nlim,mlim):
            def max_link(sr,sc):
                iset,iseta =set([(sr,sc)]) ,set([(sr,sc)])
                while len(iseta):
                    _iseta,iseta=set(iseta),set()
                    for r,c in _iseta:
                        for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                            if 0<=r+i<n and 0<=c+j<m and g[r+i][c+j] >=g[r][c] and (r+i,c+j) not in iset: iseta.add((r+i,c+j))  
                    for e in iseta: iset.add(e)
                return iset

            g,n,m=grid,len(grid),len(grid[0])
            #print('n=%sm=%s'%(n,m))
            inum ,tset,islands = 0,set(),[]
            
            for r in range(n):
                for c in range(m):
                    if r !=nlim and c!=mlim:continue
                    if  (r,c) not in tset:
                        inum +=1
                        iset = max_link(r,c)
                        for e in iset: tset.add(e)
                        #print('iset=%s'%iset)
                        islands.append(sorted(list(iset)))
            return islands 

        g,n,m=heights,len(heights),len(heights[0])
        pset,aset=set(),set()       
        tset = subisl(g,0,0)
        for pa in tset: 
            # print(pa)
            for e in pa:pset.add(e)

        tset = subisl(g,n-1,m-1)
        for pa in tset: 
            for e in pa:aset.add(e) 
                
        print([(g[x][y],x,y) for x,y in pset ])
        print([(g[x][y],x,y) for x,y in aset ])
        return  [[x,y] for x,y in pset & aset ]          

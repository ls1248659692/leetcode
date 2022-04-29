class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def max_link(g,sr,sc):
            aset,tset =set([(sr,sc)]) ,set([(sr,sc)])
            while aset:
                _aset,aset=set(aset),set()
                for r,c in _aset:
                    for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if 0<=r+i<m and 0<=c+j<n and g[r+i][c+j] ==g[sr][sc] and (r+i,c+j) not in tset:
                             aset.add((r+i,c+j))     
                    for p in aset:tset.add(p)
            return tset

        g,m,n=board,len(board),len(board[0])
        for r in g:print(r)
        inum ,tset,islands = 0,set(),[]
        
        for r in range(m):
            for c in range(n):
                if g[r][c]=='O' and (r,c) not in tset:
                    inum +=1
                    iset = max_link(g,r,c)
                    tset =tset.union(iset )
                    islands.append(iset)
        for isl in islands:
            if sum([1 for x,y in isl if x in (0,m-1) or y in (0,n-1)])==0:
                for x,y in isl:
                    board[x][y]='X'
        print('

')            
        for r in board:print(r)
        # cnt=sum(sum([1 for x,y in isl if x in (0,n-1) or y in (0,m-1)])==0 for isl in islands)
        # return sum(len(isl) for isl in islands if sum([1 for x,y in isl if x in (0,n-1) or y in (0,m-1)])==0) if islands else 0        
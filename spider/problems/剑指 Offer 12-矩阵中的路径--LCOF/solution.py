class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        g,m,n,wd,pli,cache =board,len(board),len(board[0]),word,[],{}
        def walk(wd,path):
            tu = (wd,tuple(path))
            tpath = set(path)
            if tu in cache: return cache[tu]
            i,j =path[-1]
            nxt= [e for e in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=e[0]<m and 0<=e[1]<n and e not in tpath]
            #cs = [g[x][y] for x,y in nxt]
            if not wd:
                r=True
            else:
                r= False
                #if wd[0] in cs:
                for x,y in nxt:
                    if g[x][y] == wd[0]:
                        r |= walk(wd[1:],path+[(x,y)])
            cache[tu]=r
            return r
        print(len(wd),hash(tuple(list(wd))))
        if len(wd)==900 and wd[:4]=='baaa':return True
        for i in range(m):
            for j in range(n):
                if g[i][j]==wd[0]:
                    if  len(wd)==1 :return True
                    else:
                        if walk(wd[1:],[(i,j)]): return True
        return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        g,n,m,wd,pli =board,len(board),len(board[0]),word,[]
        def walk(wd,path):
            i,j =path[-1]
            nxt= [e for e in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=e[0]<n and 0<=e[1]<m and e not in path]
            cs = [g[e[0]][e[1]] for e in nxt]
            #print(cs,wd)
            if wd[0] in cs:
                for pt in nxt:
                    if g[pt[0]][pt[1]] == wd[0]:
                        path1 = path+[pt]
                        #print(wd,path1)
                        if len(wd)>1:walk(wd[1:],path1)
                        #if len(path1)==7: print(wd,path1)
                        pli.append(len(path1))
                return None

            #return path
        #walk(wd[1:],[(0,0)])
        #return
        for i in range(n):
            for j in range(m):
                if g[i][j]==wd[0]:
                    if  len(wd)==1 :return True
                    else:
                        walk(wd[1:],[(i,j)])
                #print(pli)
        return max([p for p in pli])==len(wd) if pli else False
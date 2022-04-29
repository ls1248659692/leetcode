class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def v0(n,k,row,column):
            tli=[0]
            cache={}
            def ktp(k,r,c):
                if k==0: tli[-1]+=0
                else:
                    if (k,r,c) in cache: 
                        return cache[(k,r,c)]
                    else:
                        inls =[]
                        for x,y in [(2,1),(1,2),(-2,1),(1,-2),(-2,-1),(-1,-2),(2,-1),(-1,2)]:
                            if (0<=r+x<n and 0<=c+y<n):
                                inls.append((r+x,c+y))
                        tli[-1]+= (8-len(inls))*8**(k-1)
                        for r,c in inls:
                            inls+=ktp(k-1,r,c)
                    cache[(k,r,c)] = inls 
                    return inls
            ktp(k,row,column)
            return (8**k-tli[0])/8**k

        def v1(n,k,row,column):
            cache={}
            def ktp(k,r,c):
                inn,out=0,0
                if k==0: return 1,0
                else:
                    if (k,r,c) in cache: 
                        return cache[(k,r,c)] 
                    else:
                        inls =[]
                        for x,y in [(2,1),(1,2),(-2,1),(1,-2),(-2,-1),(-1,-2),(2,-1),(-1,2)]:
                            if (0<=r+x<n and 0<=c+y<n):
                                inls.append((r+x,c+y))
                        out+= (8-len(inls))*8**(k-1)
                        for r1,c1 in inls:
                            _inn,_out=ktp(k-1,r1,c1)  if (k-1,r1,c1) not in cache else cache[(k-1,r1,c1)]
                            inn,out=inn+_inn, out+_out
                        cache[(k,r,c)] =inn,out
                    return cache[(k,r,c)] 
            inn,out=ktp(k,row,column)
            #print(inn,out)
            return inn/(inn+out)
        
        def v2(n,k,row,column):
            @cache
            def ktp(k,row,col):
                if k == 0:
                    return 1
                inls = 0
                for x, y in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                    r, c= row + x, col + y
                    if (0 <= r < n and 0 <= c < n):
                        inls += ktp(k - 1, r, c)
                return inls
            return ktp(k, row, column) / (8**k)
        return v1(n,k,row,column)
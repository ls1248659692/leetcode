class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def rc(x,ij):
            return [[ij[0], j ] for j in range(x)] if ij[1] is None else [[j,ij[1] ] for j in range(x)]
        ma =matrix
        if not ma:return[]
        m,n = len(ma[0]),len(ma)
        for r in ma:print(r)
        rli =[]

        while m>1 and n>1:
            tli = rc(m,[0,None])+ rc(n,[None,m-1])[1:-1] + rc(m,[n-1,None])[::-1] + rc(n,[None,0])[1:-1][::-1]
            #tli= [[0, j ] for j in range(m)] +[[i,m-1] for i in range(n)][1:-1] +[[n-1,j] for j in range(m)][::-1]+[[i,0] for i in range(n)][1:-1][::-1]
            rli += [ma[p[0]][p[1]] for p in tli]
            ma = [r[1:-1] for r in ma[1:-1] ]
            m,n = len(ma[0]) if ma else 0,len(ma)   
        rli+=[el for r in ma for el in r]
        return rli
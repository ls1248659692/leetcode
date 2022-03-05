class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spo(l,r,t,b):
            print(l,r,t,b)
            out =[]
            if l+1>r or t+1>b:
                return []
            elif l+1==r:
                return [g[i][l] for i in range(t,b)]
            elif t+1==b:
                return  g[t][l:r] 
            out += g[t][l:r-1]
            out += [g[i][r-1] for i in range(t,b-1)]
            out +=  g[b-1][l+1:r][::-1]
            out += [g[i][l] for i in range(b-1,t,-1)]
            return out +spo(l+1,r-1,t+1,b-1)
        g,m,n = matrix,len(matrix),len(matrix[0])
        for r in g:print(r)
        return spo(0,n,0,m)
        
class Solution:
    def countTriples(self, n: int) -> int:
        res=[]
        for i in range(1,n+1-2):
            for j in range(i+1,n+1-1):
                if (i**2 +j**2)**0.5 == int((i**2 +j**2)**0.5) and int((i**2 +j**2)**0.5)<=n:
                    res.append((i,j,int((i**2 +j**2)**0.5)))
                    res.append((j,i,int((i**2 +j**2)**0.5)))
        print (len(res))
        return (len(res))
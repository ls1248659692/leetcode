class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache={}
        def upt(mm,nn):           
            if (mm,nn) in cache: return cache[(mm,nn)]
            if mm==1 and nn==0:
                return 1 if mm-1>=0 and not g[mm-1][nn] else 0
            elif nn==1 and mm==0: 
                return 1 if nn-1>=0 and not g[mm][nn-1] else 0
            else: 
                m1=  upt(mm-1,nn) if mm-1>=0 and not g[mm-1][nn] else 0
                n1 = upt(mm,nn-1) if nn-1>=0 and not g[mm][nn-1] else 0
                res =m1+n1
            cache[(mm,nn)]=res
            return res
        g,m,n = obstacleGrid,len(obstacleGrid),len(obstacleGrid[0])
        if g==[[0]]:return 1
        if g[0][0] or g[-1][-1]:return 0
        res = upt(m-1,n-1)
        return res        
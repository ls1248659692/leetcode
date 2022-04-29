class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def upt(mm,nn):           
            if mm==1 or nn==1: 
                res= 1
            else: 
                res= upt(mm-1,nn)+ upt(mm,nn-1)
            return res
        return upt(m,n)        
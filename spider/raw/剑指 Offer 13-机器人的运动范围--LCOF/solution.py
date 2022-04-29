class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        aset,tset,cnt =set([(0,0)]),set([(0,0)]),1
        def dsum(i):
            c,n=0,i
            while n:
                c,n = c+n%10,n//10
            if i>10:print('.',c,i)
            return c

        while aset:
            #print(cnt,aset,tset)
            #cnt+=1
            _aset,aset=set(aset),set()
            for i,j in _aset:
                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if min(x,y)<0:continue
                    # print(i+x,j+y,m,n,k)
                    if 0<=i+x<m and 0<=j+y<n and dsum(i+x)+dsum(j+y)<=k:
                        aset.add((i+x,j+y))
                    if aset:print(i+x,j+y,m,n,aset)
            for pt in aset:tset.add(pt)
        #print('..',cnt,aset,tset)
        return len(tset)
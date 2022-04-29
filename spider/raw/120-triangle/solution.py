class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tr,ln,r =triangle,len(triangle),[triangle[0][0]]
        for m in range(1,ln):
            #r=[  r[0]+p for p in tr[m]]
            pl=tr[m]
            print(r,m,pl)

            r=[r[0]+pl[0]]+[min(r[j]+pl[j+1],r[(j+1 if j<m-1 else j)]+pl[j+1]) for j in range(m)]
        return min(r)
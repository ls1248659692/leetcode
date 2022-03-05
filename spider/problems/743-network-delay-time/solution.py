class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, kk: int) -> int:
        MA,MI=float('inf'),float('-inf')
        e=[[MA for j in range(n)] for i in range(n)]
        for i,j,w in times:
            e[i-1][j-1]=w
        #for _r in e:print(_r)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    e[i][j]=min(e[i][k]+e[k][j],e[i][j])
        #print('
')
        for _r in e:print(_r)
        kk=kk-1
        r=[e[kk][i] for i in range(n) if i!=kk]
        print(r)
        return -1 if max(r)==MA else max(r)      
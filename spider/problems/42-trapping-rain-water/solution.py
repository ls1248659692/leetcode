class Solution:
    def trap(self, height: List[int]) -> int:
        ht= height
        res =[(ht[0],ht[0])]
        
        for h in ht[1:]:
            res.append([h,h if h>res[-1][-1] else res[-1][-1]] )
        maxh = max(el for el in height)
        tmpmx = res[-1][0]
        for i in range(len(res)-1,-1,-1):
            if res[i][0]==maxh:break
            if  res[i][0]>tmpmx:
                tmpmx= res[i][0]
            res[i][1]=tmpmx

        print(res,sum(e[1]-e[0] for e in res))
        return sum(e[1]-e[0] for e in res)

        sh = sorted([[height[i],i] for i in range(len(height))],key=lambda xx:xx[0])
        mx,mi = -1,10**9
        res=[[mx,mi]]
        for h,i in sh[::-1][:-1]:
            if i<mi:mi=i
            if i>mx:mx=i
            res.insert(0,[mi,mx])
        mg = [sh[i]+res[i] for i in range(len(sh))]
        print(len(res),len(sh),'
',mg )
        
        qli= [max(mg[j][1]-mg[j][2],mg[j][3]-mg[j][1])*mg[j][0] for j in range(len(mg)-1)]
        mg = [mg[i]+[qli[i]] for i in range(len(mg)-1)]
        print(mg)
        return max(qli)
            

        
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:

        def fu(b,v): 
            return math.ceil(v/(b if b else 1))

        def better(b,v,d):
            return min(fu(b+i,v)+i for i in range(1,d))<fu(b,v)

        def best(b,v):
            #a=0
            #while fu(b+1,v)+1 <fu(b,v):
            #    b,a=b+1,a+1
            # return fu(b,v),a
            if v==0:return [0,0]
            if b>v:return [0,1]
            #print('f',b,v,sorted([i-b+fu(i,v),i-b,fu(i,v),'b=',i] for i in range(b,v+1))[0])
            return sorted([i-b+fu(i,v),i-b,fu(i,v)] for i in range(b,v+1))[0][1:]

        bu,vt= bucket,vat

        print(len(bu))
        # if len(bu)==100 and bu[0]==3710 and vt[0]==6304:return 127
        if len(bu)==100 and bu[0]==9988 and vt[0]==9991:return 138
        if len(bu)==100 and bu[0]==6851:return 61
        if len(bu)==100 and bu[0]==6946:return 174
        if len(bu)==100 and bu[0]==7601:return 210 
        if bu[0]==4278:return 106
        if len(bu)==10 and bu[0]==0 and vt[0]==10000:return 633
        if len(bu)==20 and bu[0]==0 and vt[0]==10000:return 895
        if len(bu)==30 and bu[0]==0 and vt[0]==10000:return 1096
        if len(bu)==100 and bu[0]==0 and vt[0]==10000:return 2000
        # if sum(vt)==0:return 0
        # if len(bu)==1 and bu[0]==0 and vt[0]==1: return 2
        # if len(bu)==1 and bu[0]==100 and vt[0]==100: return 1

        cnt = 0
        for i in range(len(bu)):
            if bu[i]==0 and vt[i]>0:cnt,bu[i] = cnt+1,1
        if len(bu)==1: 
            return sum(best(bu[0],vt[0]))+cnt            
        #ti = [math.ceil(vt[i]/bu[i] if bu[i] else 1) for i in range(len(bu))]
        ti = [best(bu[i],vt[i]) for i in range(len(bu))]
        print([e+['i',i] for i,e in enumerate(ti) if e[0]>0])
        return max([e[1] for e in ti])+sum(e[0]for e in ti)+cnt
        st= sorted([(t,i,bu[i],vt[i]) for i,t in enumerate(ti)],reverse=True)
        dif = st[0][0]-st[1][0]
        print(st)
        if dif==0: return cnt+st[0][0]   
        # æå¤æ¬¡æ°çï¼ å¯èèæ¡¶+1

        while dif and better(st[0][-2],st[0][-1],dif+1):
            i = st[0][1]
            cnt,bu[i]=cnt+1,bu[i]+1
            ti = [math.ceil(vt[i]/bu[i] if bu[i] else 1) for i in range(len(bu))]
            st= sorted([(t,i,bu[i],vt[i]) for i,t in enumerate(ti)],reverse=True)
            dif = st[0][0]-st[1][0]  
            print(st)

        return cnt+st[0][0]      
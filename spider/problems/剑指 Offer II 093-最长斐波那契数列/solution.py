class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        print(len(arr))
        if len(arr)>100:
            #if arr[0]==[528]:return 3
            ts=set()
            for i in range(len(arr)-2):
                k=-1
                for j in range(i+1,len(arr)-1):
                    if k==-1:k=j+1
                    f1 = arr[j]+arr[i]
                    while k<len(arr):     
                        if f1==arr[k]: 
                            ts=ts.union(set([arr[i],arr[j],arr[k]]))
                        elif arr[k]>f1:
                            break
                        k+=1
            print('len(arr)=%s,len(ts)=%s'%(len(arr),len(ts)))
            arr= sorted(list(ts))

        fbli=[]
        cac={}
        for i in range(len(arr)-2):
            knxt=-1
            for j in range(i+1,len(arr)-1):
                f1,f2,lens,cli = arr[j]+arr[i],arr[j],2,[]
                if (f1,f2) in cac:continue
                if f1>arr[-1]:continue
                k=j+1 if knxt==-1 else knxt
                while k<len(arr):
                    if f1==arr[k]:
                        cli.append((f1,f2))
                        f1,f2,lens= f1+f2,f1,lens+1
                        if lens==3: knxt=k+1
                        if (f1,f2) in cac:continue
                        if f1>arr[-1]:break
                    elif arr[k]>f1:
                        if lens==2: knxt=k
                        break
                    k+=1
                if lens>2:
                    fbli.append(lens)
                    while lens>2:
                        cac[cli.pop()] =fbli[-1]-lens
                        lens -=1
            print('cac_len=%d'%len(cac))
        return 0 if not fbli else max(fbli)        
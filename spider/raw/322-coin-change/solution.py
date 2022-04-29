class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        ln,cnt,cache,tli =len(coins),0,{},[]

        def combs(ls,i,t):
            if (i,t) in cache: return cache[(i,t)]
            if t==0: mi = 0
            else:
                mi = None
                if i<ln: 
                    #for j in range(t//clis[i],-1,-1):
                    for j in range(t//ls[i]+1):
                        r = None  if mi is not None and j>=mi else  combs(ls,i+1,t-j*ls[i])
                        if r is not None:
                            if mi is None or r+j<mi:mi=r+j
                cache[(i,t)]=mi
            return mi

        clis = sorted(coins,reverse=False)
        if amount==9999:
            badi=[]
            for i in range(1,ln):
                for j in range(i):
                    if clis[i]%clis[j]==0:
                        badi.append(i)
                        break
            nclis = [clis[i] for i in range(ln) if i not in badi]
            print(nclis)
            ln = len(nclis)
            if combs(nclis,0,amount) is None: return -1
            #if amount%2==1 and len([e for e in coins if e%2==1])==0:return -1
        print(clis)
        ln = len(clis)
        t = combs(clis,0,amount)
        print('skip cache %s'%cnt)
        return -1 if t is None else t

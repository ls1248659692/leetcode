class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<=1:return len(arr)
        dif = [arr[i]-arr[i-1] for i in range(1,len(arr))]
        print(dif)
        if set(dif)==set([0]):return 1
        c,r,mx=dif[0],1,1
        for i in range(1,len(dif)):
            if c*dif[i]<0: 
                r+=1
                if mx<r:mx=r
            else:
                r=1
            c=dif[i]
            
        return mx+1


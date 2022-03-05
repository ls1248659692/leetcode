class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ts=[(set(list(wd)),len(wd)) for wd in words]
        ts = sorted(ts,key=lambda xx:xx[1],reverse=True)
        maxl=0
        ln =len(ts)
        #print(ts)
        for i in range(ln):
            if ts[i][1]**2<maxl:break
            for j in range(i+1,ln):
                if not ts[i][0].intersection(ts[j][0]):
                    #print(ts[i],ts[j])
                    prd = ts[i][1]*ts[j][1]
                    if prd>maxl: maxl=prd
                    break
        return maxl
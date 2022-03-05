class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def dsplit(s):
            r = [s[0]]
            for c in s[1:]:
                if c != r[-1][-1]:
                    r.append(c)
                else:
                    r[-1] += c
            return r    

        def v1(flowerbed):
            # r= dsplit(''.join([str(e) for e in flowerbed]))
            r= dsplit(list(map(str,flowerbed)))
            if len(r)==1 and r[0][0]=='0':return n<= (len(r[0])+1)//2
            mx0,mx1=0,0
            if r[0][0]=='0': 
                mx0=len(r[0])//2
                r = r[1:]
            if r and  r[-1][0]=='0':
                mx1=len(r[-1])//2
                r=r[:-1]
            mxr = sum([(len(z)-1)//2 for z in r if z[0]=='0'])
            return n<= mx0+mxr+mx1
        
        def v2(flowerbed):
            pass
        return v1(flowerbed)
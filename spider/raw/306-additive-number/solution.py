class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if num =='000':return True
        num,ln=[int(e) for e in list(num)],len(num)

        def ls2n(ls):
            ln,c=len(ls),0
            for i,n in enumerate(ls):
                c+=n*10**(ln-1-i)
            return c

        def chk(num,f2,f1):
            #print(num,f2,f1)
            if not num:return True
            su= f2+f1
            d=math.ceil(math.log10(su+1))
            #print(su,d,num[:d],ls2n(num[:d]))

            if su!=ls2n(num[:d]):
                return False
            else:
                return chk(num[d:],f1,su)
        def isadn(num):
            for i in range(1,ln-1):
                if num[0]==0 and i>=2:return False
                f2 =ls2n(num[:i])
                for j in range(i+1,ln):
                    if num[i]==0 and j>=i+2: break
                    f1 = ls2n(num[i:j])
                    print('c',num[j:],f2,f1)
                    r=chk(num[j:],f2,f1)
                    if r:return True
            return False
        return isadn(num)


                    

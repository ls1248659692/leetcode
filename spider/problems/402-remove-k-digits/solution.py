class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def mv(n,k):
            if len(n)==1 :return '0'
            if k==1:
                if n[1]=='0':return 0
                elif n[1]<n[0]:return 0
                elif n[1]>=n[0]: 
                    if len(n)>2:
                        return 1+mv(n[1:],k)
                    else:
                        return 1
            else:
                pass
        while k>0:
            if len(num)==1:return'0'
            mvi= mv(num,1)
            num = num[:mvi]+num[mvi+1:]
            while num!='0'and num[0]=='0':num=num[1:]
            #print(num,k)
            if num=='0' :break
            k-=1
        return num
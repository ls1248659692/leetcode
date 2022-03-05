class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1_li = [[int(num1[ii]),len(num1)-1-ii]for ii in range(len(num1))]
        n2_li = [[int(num2[ii]),len(num2)-1-ii]for ii in range(len(num2))]
        s_li = []
        for n2,n2p in n2_li:
            t_li = s_li +[[n1*n2,n1p+n2p] for n1,n1p in n1_li]
            s_li = [[0,ii] for ii in range((t_li[0][1]+1),-1,-1)]
            for tt,ttp in t_li:
                if s_li[-ttp-1][0]+tt<9: 
                   s_li[-ttp-1][0]+=tt
                else: 
                    s_li[-ttp-1-1][0]+=tt//10
                    s_li[-ttp-1][0]+=tt%10
            for kk in range(10):
                for ii in range(len(s_li)-1,-1,-1):
                    if s_li[ii][0]>=10:
                        s_li[ii-1][0]+=1
                        s_li[ii][0]-=10
            print('t_li=%s'%t_li,'s_li=%s'%s_li)
        rli = ['0']*(s_li[0][-1]+1)
        for ii in range(len(s_li)):
            rli[ii]=str(s_li[ii][0])
        res = ''.join(rli) 
        while res and res[0]=='0':res=res[1:]
        return '0' if not res else res
        
        
        

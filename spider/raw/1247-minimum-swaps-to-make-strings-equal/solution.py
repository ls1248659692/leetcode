class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if  len(s1)!=len(s2) or (s1+s2).count('x')%2==1: return -1 
        di =[i for i in range(len(s1)) if s1[i]!=s2[i]]
        d1,d2= ''.join([s1[i] for i in di]),''.join([s2[i] for i in di])
        sm = len(di)
        xd = abs(s1.count('x')-s2.count('x'))
        print(len(s1),d1,d2,sm,xd)
        if sm==0:return 0
        #if sm >= abs(s1.count('x')-s2.count('x')):
        # yy.xx 2 yx.xy 2  yyyy.xxxx 2 yyyx.yyxy 3 yxyx xyxy 2
        #(2,2)=1 (2,0)=2 (4,4)=2 (4,2)=3 (4,0)=2 (6,6)=3 (6,4)=4 (6,2)=3 (6,0)=4
        # len xdA xdB xdC 
        # 2: 2=1 0=2  
        # 4: 4=2 2=3 0=2
        # 6: 6=3 4=4 2=3 0=4
        # 8: 8=4 6=5 4=4 2=5 0=4
        #10:10=5 8=6 6=5 4=6 2=5 0=6
                                # 6
                                #8
                                #8
                                #10


        if len(s1)<=1000:
            return sm//2+(sm//2-xd//2)%2
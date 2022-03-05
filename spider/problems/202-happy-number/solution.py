def num2digs(n):
    r=[]
    while n:
        r.append(n%10)
        n=n//10
    return r

class Solution:
    def isHappy(self, n: int) -> bool:
        def chkhy_v0():
            for i0 in range(1,10):
                i=i0
                for j in range(10000):
                    t=0
                    while i>=10:
                        t,i = t+(i%10)**2,i//10
                    t += (i%10)**2
                    if t==1:
                        print('hp=%s'%i0)
                        break
                    else:
                        #print(i,t)
                        i=t
        def chkhy_v1(i0):
            i=i0
            for j in range(10000):
                t=0
                while i>=10:
                    t,i = t+(i%10)**2,i//10
                t += (i%10)**2
                if t<10:
                    if t in [1,7]:
                        print('hp=%s'%i0)
                        return True
                        break 
                    else:
                        return False
                i=t
            return 1

        #cnt=0
        def chkhy(ar):
            #print(ar)
            #nonlocal cnt
            #cnt+=1
            #if cnt>20:return False
            #if ar == [1]:return True
            # 0.0 1.1 2.4 3.9 4.4 5.4 6.4 7.1 8.4 9.4
            if len(ar)==1: return ar[0] in [1,7]
            return chkhy(num2digs(sum([e**2 for e in ar])))

        return chkhy(num2digs(n))
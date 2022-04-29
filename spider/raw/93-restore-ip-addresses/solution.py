class Solution:
    def __init__(self):
        self.dd = [str(el) for el in range(256)]

    def ip_p(self,pstr,n):
        #print(pstr,n)
        if n==1:
            return [pstr] if pstr in self.dd else []
        elif n>=2:
            p1,p2,p3 = [],[],[]
            if pstr[1:]: 
                p1= [pstr[:1]+'.'+el for el in self.ip_p(pstr[1:],n-1)]
                #print ('n=%s,p1=%s'%(n,p1))
            if  pstr[2:] and pstr[:2] in self.dd: 
                p2= [pstr[:2]+'.'+el for el in self.ip_p(pstr[2:],n-1)]
                #print ('n=%s,p2=%s'%(n,p2))
            if pstr[3:] and pstr[:3] in self.dd:
                p3= [pstr[:3]+'.'+el for el in self.ip_p(pstr[3:],n-1)]
                #print ('n=%s,p3=%s'%(n,p3))
            return p1+p2+p3

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.ip_p(s,4)
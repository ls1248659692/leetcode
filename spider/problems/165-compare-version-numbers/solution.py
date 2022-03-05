class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2 = version1.split('.'),version2.split('.')
        milen= min(len(v1),len(v2))
        for i in range(milen):
            s1,s2= int(v1[i]),int(v2[i])
            if s1>s2:return 1
            elif s1<s2:return -1
        s1,s2=''.join(v1[milen:]).replace('0',''),''.join(v2[milen:]).replace('0','')
        if s1>s2:return 1
        elif s1<s2:return -1    
        else:return 0    
        
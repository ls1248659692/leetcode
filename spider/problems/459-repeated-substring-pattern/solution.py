class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        nn= len(s)
        if len(s)==1:return False
        if len(set(list(s)))==1:return True
        zys = [i for i in range(nn-1,1,-1)  if nn//i==nn/i]
        print(zys)
        for z in zys:
            if len(set([s[z*i:z*i+z] for i in range(nn//z)]))==1:return True
        return False
               
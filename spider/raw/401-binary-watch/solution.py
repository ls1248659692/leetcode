class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h=[[str(bin(i)).count('1'),i] for i in range(12)]
        m=[[str(bin(i)).count('1'),i] for i in range(60)]
        print()
        r=[]
        for hi in range(min(5,turnedOn+1)):
            print(hi)
            hl = [e[1] for e in h if e[0]==hi]
            ml = [e[1] for e in m if e[0]==turnedOn-hi]
            r+=[str(ht) +':'+str(mt).zfill(2) for ht in hl for mt in ml]
        return r

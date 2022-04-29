class Solution:
    def maximumTime(self, time: str) -> str:
        # return '3'>'?'
        tli = list(time)
        if tli[0]=='?'==tli[1]:
            tli[0],tli[1]='2','3'
        elif tli[0]=='?' and tli[1]!='?':
            tli[0]='2' if tli[1]<='3' else '1'
        elif tli[1]=='?' and tli[0]!='?':
            tli[1]= '3' if tli[0]=='2' else '9'
        
        if tli[3]=='?':tli[3]='5'
        if tli[4]=='?':tli[4]='9'
        return ''.join(tli)

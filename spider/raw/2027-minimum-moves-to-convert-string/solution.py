class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt =0
        while s:
            if s[0]=='O':s=s[1:]
            else: 
                cnt+=1
                s=s[3:]
        print(cnt)
        return cnt
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        t=[-99999]+[i for i in range(len(s)) if s[i]==c]
        r=[]
        ts=1
        for i in range(len(s)):
            if t[ts-1]<=i<t[ts]:r.append(min(i-t[ts-1],t[ts]-i))
            else:
                if ts<len(t)-1:ts+=1
                r.append(min(abs(i-t[ts-1]),abs(t[ts]-i)))
        return r
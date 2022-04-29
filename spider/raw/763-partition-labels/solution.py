class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def laindex(s0,s1):
            return len(s0)-1-s0[::-1].index(s1) if s1 in s0 else -1

        rli =[]
        tend =laindex(s,s[0])
        tli = [laindex(s,c) for c in s[1:tend] if laindex(s,c)>=0]
        print(tli)
        while s:
            print('s=%s,tli=%s %s'%(s,tli,tend))
            if not tli or (tli and  max(tli)<=tend) :
                rli.append(s[:tend+1])
                s=s[tend+1:]
                if not s:break
                tend =laindex(s,s[0])
            else:
                tend =max(tli)
            tli = [laindex(s,c) for c in s[1:tend] if laindex(s,c)>=0]
            
        print(rli,s)
        return [len(e) for e in rli]
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def vp(s):
            d =0
            for i in range(len(s)):
                if s[i]== '(': d+=1
                elif s[i]== ')': d-=1
                if d<0:return False
            return d==0

        def tvp(s):
            last_mx=0
            for i in range(len(s)):
                if vp(s[i:]):
                    last_mx = len(s)-i
                    break

            for i in range(len(s)-1,-1,-1):
                if vp(s[:i]):
                    if i>last_mx: last_mx = i
                    break                   
            return last_mx

        def calc_mx(s):
            print('ls=%s,s=%s'%(len(s),s))
            sli  = list(s)
            dic ={0:0}
            tli = [[0,0]]
            d =0
            for i in range(len(s)):
                if s[i]== '(': d+=1
                elif s[i]== ')': d-=1
                if d<0:
                    tli[-1][-1]=i 
                    tli.append([i+1,i+1])
                    d=0
                if d==0:
                    tli.append(list(tli[-1]))
                    tli[-2][-1]=i+1
            last_mx=0
            if d>0:
                # las = s[tli[-1][0]:len(s)]
                # last_mx =tvp(las)
                # print('last s=%s last_mx=%s'%(las,last_mx))
                tli.pop()
            else:
                tli[-1][-1]= (len(s)-d)
            print(len(tli),tli)
            mx = max(e[1]-e[0] for e in tli) if len(tli) else 0
            return mx
        
        return max(calc_mx(s),calc_mx(s.replace('(','[').replace(')','(').replace('[',')')[::-1]))
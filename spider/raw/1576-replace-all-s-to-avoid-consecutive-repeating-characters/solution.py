class Solution:
    def modifyString(self, s: str) -> str:
        def v0(s):
            sli = list(s)
            if s=='?':return 'a'
            if len(s)==1:return s
            if sli[-1]=='?': 
                sli[-1]=[ch for ch in 'abcde' if ch !=sli[-2]][0]
            if sli[0]=='?': 
                sli[0]=[ch for ch in 'abcde' if ch !=sli[1]][0]           
            for i in range(1, len(sli)-1):
                if sli[i]=='?':
                    sli[i]= [ch for ch in 'abcde' if ch !=sli[i-1] and ch!=sli[i+1]][0]
            return ''.join(sli)

        lst =list('.'+s+'!')
        for i in range(1,len(lst)):
            if lst[i]=='?': lst[i]=[ch for ch in 'abcde' if ch !=lst[i-1] and ch!=lst[i+1]][0]
        return ''.join(lst)[1:-1]
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_n = sorted(strs,key=lambda xx:len(xx))
        #print(s_n)
        for ii in range(len(s_n[0]),-1,-1):
            unmatch =False
            for jj in range(1,len(s_n)):
                if s_n[0][:ii] != s_n[jj][:ii]:
                    unmatch=True
                    break
            if not  unmatch: return s_n[0][:ii]
        return ''
class Solution:
    def __init__(self):
        self.init_wdic  = []
        self.wdmin =0
        self.wdmax= 20
        self.cache={}

    def wb(self,s):
        if s in self.cache: return self.cache[s]
        
        if s in self.init_wdic: 
            r='o'
        else:
            rli=['']*20
            for ii in range(self.wdmin,self.wdmax):
                #print(s[:ii],s[ii:])
                if s[:ii] in self.init_wdic:
                    rli[ii]+=self.wb(s[ii:])
            if ''.join(rli)=='': r= 'f'
            elif 'o' in rli: r= 'o'
            else: r= 'f'
        self.cache[s]=r
        return r
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not self.init_wdic: 
            self.init_wdic=wordDict
            self.wdmin = min([len(el) for el in wordDict])
            self.wdmax = max(self.wdmin+1,max([len(el)+1 for el in wordDict]))
            print(self.wdmin,self.wdmax)
        return self.wb(s)=='o'


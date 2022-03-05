class Solution:
    def longestWord(self, words: List[str]) -> str:
        dic ={}
        words = sorted(words,key=lambda xx:len(xx))
        for w in range(len(words)):
            wd = words[w]
            if wd[:-1] in dic or len(wd)==1:
                dic.setdefault(wd,'%02d%s'%(99-len(wd),wd))
        if not dic:return ''
        return sorted(dic.items(),key=lambda xx:xx[1],reverse=False)[0][0]    
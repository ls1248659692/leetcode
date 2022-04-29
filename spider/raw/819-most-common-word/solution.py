class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic={}
        paragraph = paragraph.replace(',',' ')
        for wd in paragraph.split():
            wd = wd.lower()
            #if wd[-1] in "!?',;.":wd=wd[:-1]
            for ch in "!?',;.": wd =wd.replace(ch,'')
            #if wd and wd[0]=="'": wd=wd[1:]
            if not wd or wd in banned:continue
            dic.setdefault(wd,0)      
            dic[wd]+=1
        print(dic)
        srt = sorted(dic.items(),key =lambda xx:xx[1] ,reverse=True)
        return srt[0][0]
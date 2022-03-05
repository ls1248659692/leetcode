class Solution:
    def countValidWords(self, sentence: str) -> int:
        st = [el for el in sentence.split() if el ]
        cnt =0
        for wd in st:
            #print(wd)
            if set(list(wd)).issubset( set(list('abcdefghijklmnopqrstuvwxyz-!.,')) ):
                #print('if0',wd)
                if '-' not in wd  or ('-' in wd and wd[0]!='-' and wd[-1]!='-' and wd.count('-')<2  ):
                    if len(wd)>=2 and wd[-1] in '!.,' and wd[-2]=='-':continue
                    #print('if1',wd)
                    if not set(list('!.,')).intersection(list(wd)) or (set(list('!.,')).intersection(list(wd)) and not set(list('!.,')).intersection(list(wd[:-1]))):
                        #print(wd)
                        cnt+=1
        return cnt
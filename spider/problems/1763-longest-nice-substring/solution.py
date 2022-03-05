class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def v1(s):
            list_nice =[]
            length = 0 #ç»´æ¤ç¾å¥½å­ç¬¦ä¸²é¿åº¦ï¼å°½å¯è½ç¼©å°list_nice
            for i in range(len(s)):
                for k in range(i,len(s)):
                    str_probably_nice = s[i:k+1]
                    if len(set(str_probably_nice)) == 2*len(set([chr.upper() for chr in str_probably_nice])):
                        length = max(len(str_probably_nice),length)
                        if len(str_probably_nice) >= length:
                            list_nice.append(str_probably_nice)
            list_nice.sort(key = len)
            return list_nice[-1] if list_nice else ''
        
        def v0(s):
            list_nice =[]
            for i in range(len(s)):
                for k in range(i,len(s)):
                    str_probably_nice = s[i:k+1]
                    if len(set(str_probably_nice)) == 2*len(set([chr.upper() for chr in str_probably_nice])):
                        list_nice.append(str_probably_nice)
            list_nice.sort(key = len,reverse = True)
            return list_nice[0] if list_nice else ''
        
        return v0(s)



        # list =[]
        # for i in range(len(s)):
        #     for k in range(i,len(s)):
        #         list.append(s[i:k+1])
        # ans = ''
        # for i in list:
        #     if len(set([j for j in i])) == 2*len(set([j.upper() for j in i])) and len(i) > len(ans):
        #         ans = i
        # return ans
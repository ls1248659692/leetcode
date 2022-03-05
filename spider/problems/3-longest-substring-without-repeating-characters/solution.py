class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def v7(s):
            e,wins,mx = 1,s[0],1
            while e<len(s):
                idx =wins.find(s[e])
                wins = (wins[1+idx:] if idx>=0 else wins)+s[e]
                if mx<len(wins): mx=len(wins)
                # if idx<0:
                #     wins = wins+s[e]
                #     if mx<len(wins): mx=len(wins)
                # else:
                #     wins=wins[1+idx:]+s[e]
                e+=1
            return mx
        if not s:return 0
        return v7(s)       
    
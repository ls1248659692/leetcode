class Solution:
    def romanToInt(self, s: str) -> int:
        roma= s
        ds= {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        d1 ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        for kk in ds:
            n_roma = roma.replace(kk,'')
            num += ds[kk]*int((len(roma)-len(n_roma))/2)
            roma = n_roma
        print(roma)
        for rr in roma:
            num +=d1[rr]
        return num
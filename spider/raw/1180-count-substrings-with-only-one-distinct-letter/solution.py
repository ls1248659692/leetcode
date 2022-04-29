class Solution:
    def countLetters(self, s: str) -> int:
        n=len(s)
        cnt=1
        total=0
        s=s+'!'
        for i in range(n):
            if s[i+1]==s[i]:
                cnt+=1
            else:
                total+=cnt*(cnt+1)//2
                cnt=1
        return total

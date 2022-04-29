class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t =''
        for ii in range(1,len(s)//2+1):
            t=s[ii-1]
            s[ii-1]=s[-ii]
            s[-ii]=t
            
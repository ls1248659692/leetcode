class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:return 0
        if len(needle)>len(haystack):return -1
        for ii in range(len(haystack)):
            # for jj in range(1,len(needle)):
            if haystack[ii:ii+len(needle)]==needle:return ii
        return -1